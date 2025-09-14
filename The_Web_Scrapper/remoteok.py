import requests
import json


def extract_jobs(term):
    """RemoteOK API를 사용하여 작업 검색"""
    url = "https://remoteok.com/api"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            jobs = []
            
            # 첫 번째 항목은 헤더이므로 제외
            for job_data in data[1:]:
                # 검색어가 태그나 포지션에 포함되는지 확인
                if (term.lower() in job_data.get('tags', []) or 
                    term.lower() in job_data.get('position', '').lower()):
                    jobs.append(jobs_detail(job_data))
            
            return jobs
        else:
            print(f"Can't get jobs. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []


def jobs_detail(job_data):
    """API 데이터에서 작업 정보 추출"""
    company = job_data.get('company', 'N/A')
    position = job_data.get('position', 'N/A')
    location = job_data.get('location', 'Remote')
    job_id = job_data.get('id', '')
    link = f"https://remoteok.com/remote-jobs/{job_id}"
    
    return {
        'company': company,
        'position': position,
        'location': location,
        'link': link
    }

def get_remoteok_job(word):
    return extract_jobs(word)