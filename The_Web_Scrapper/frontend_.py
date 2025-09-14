from logging import exception
from flask import Flask, redirect, render_template, request, send_file, flash
from wanted import get_wanted_job
from saramin import get_saramin_job
from jobplanet import get_jobplanet_job
from worknet import get_worknet_job
from save import save_to_file
app = Flask(__name__)
app.config["SECRET_KEY"] = "ABCD"
db={}

@app.route("/")
def home():
    return render_template("index.html")

def filter_jobs_by_location(jobs, selected_locations):
    """선택된 지역에 따라 채용공고 필터링"""
    if not selected_locations or selected_locations == '':
        return jobs
    
    locations = [loc.strip() for loc in selected_locations.split(',')]
    filtered_jobs = []
    
    for job in jobs:
        job_location = job.get('location', '').lower()
        
        # 선택된 지역 중 하나라도 포함되면 포함
        for location in locations:
            if location.lower() in job_location or job_location in location.lower():
                filtered_jobs.append(job)
                break
    
    return filtered_jobs

@app.route("/report")
def react():
    word = request.args.get('word')
    wanted_enabled = request.args.get('wanted', 'true').lower() == 'true'
    saramin_enabled = request.args.get('saramin', 'true').lower() == 'true'
    jobplanet_enabled = request.args.get('jobplanet', 'true').lower() == 'true'
    worknet_enabled = request.args.get('worknet', 'true').lower() == 'true'
    selected_locations = request.args.get('locations', '')
    
    if word:
        word = word.lower()
        store_data = db.get(word)
        if store_data:
            jobs = store_data
        else:
            jobs = []
            
            # 선택된 사이트만 검색
            if wanted_enabled:
                wanted_jobs = get_wanted_job(word)
                jobs.extend(wanted_jobs)
                
            if saramin_enabled:
                saramin_jobs = get_saramin_job(word)
                jobs.extend(saramin_jobs)
                
            if jobplanet_enabled:
                jobplanet_jobs = get_jobplanet_job(word)
                jobs.extend(jobplanet_jobs)
                
            if worknet_enabled:
                worknet_jobs = get_worknet_job(word)
                jobs.extend(worknet_jobs)
            
            db[word] = jobs
            if (len(db[word]) == 0):
                return redirect("/sorry")
        
        # 지역 필터링 적용
        jobs = filter_jobs_by_location(jobs, selected_locations)
        
        # 출처별 통계 계산
        wanted_count = len([job for job in jobs if job.get('source') == '원티드'])
        saramin_count = len([job for job in jobs if job.get('source') == '사람인'])
        jobplanet_count = len([job for job in jobs if job.get('source') == 'JobPlanet'])
        worknet_count = len([job for job in jobs if job.get('source') == 'WorkNet'])
        
        return render_template("/report.html", 
                             word=word, 
                             number=len(jobs), 
                             jobs=jobs,
                             wanted_count=wanted_count,
                             saramin_count=saramin_count,
                             jobplanet_count=jobplanet_count,
                             worknet_count=worknet_count,
                             wanted_enabled=wanted_enabled,
                             saramin_enabled=saramin_enabled,
                             jobplanet_enabled=jobplanet_enabled,
                             worknet_enabled=worknet_enabled,
                             selected_locations=selected_locations)
    
    return redirect("/")


@app.route("/download")
def datasave():
    try:
        word = request.args.get('word')
        if not word:
            flash("검색어가 없습니다.")
            return redirect("/")
        
        word = word.lower()
        jobs = db.get(word, [])
        
        if not jobs:
            flash("다운로드할 데이터가 없습니다.")
            return redirect("/")
        
        # CSV 파일 생성
        import csv
        import io
        
        # CSV 데이터를 메모리에 생성
        output = io.StringIO()
        writer = csv.writer(output)
        
        # 헤더 작성
        writer.writerow(["Company", "Position", "Location", "Experience", "Requirements", "Main Tasks", "Salary", "Link", "Source"])
        
        # 데이터 작성
        for job in jobs:
            writer.writerow([
                job.get('company', 'N/A'),
                job.get('position', 'N/A'),
                job.get('location', 'N/A'),
                job.get('experience', 'N/A'),
                job.get('requirements', 'N/A'),
                job.get('main_tasks', 'N/A'),
                job.get('salary', 'N/A'),
                job.get('link', 'N/A'),
                job.get('source', 'N/A')
            ])
        
        # 파일명 생성
        filename = f"jobs_{word}_{len(jobs)}_results.csv"
        
        # BytesIO로 변환 (UTF-8 BOM 포함)
        output.seek(0)
        csv_data = output.getvalue()
        csv_bytes = io.BytesIO()
        csv_bytes.write('\ufeff'.encode('utf-8'))  # UTF-8 BOM
        csv_bytes.write(csv_data.encode('utf-8'))
        csv_bytes.seek(0)
        
        return send_file(
            csv_bytes,
            as_attachment=True,
            download_name=filename,
            mimetype='text/csv'
        )
        
    except Exception as e:
        print(f"CSV 다운로드 오류: {e}")
        flash("CSV 다운로드 중 오류가 발생했습니다.")
        return redirect("/")


@app.route("/sorry")
def sorry():
    return render_template("sorry.html")
        

    
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port, debug=False)