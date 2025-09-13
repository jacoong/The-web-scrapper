import requests
import json


def extract_jobs(term):
    """원티드 API를 사용하여 채용공고 검색"""
    url = "https://www.wanted.co.kr/api/v4/jobs"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "application/json",
        "Referer": "https://www.wanted.co.kr/",
    }
    
    params = {
        "country": "kr",
        "job_sort": "company.response_rate_order",
        "years": "-1",
        "locations": "all",
        "limit": "50"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            jobs = []
            
            if 'data' in data:
                for job_data in data['data']:
                    # 검색어가 제목이나 회사명에 포함되는지 확인
                    # 개발자 관련 키워드들로 필터링 완화
                    position = job_data.get('position', '').lower()
                    company = job_data.get('company', {}).get('name', '').lower()
                    
                    # 개발자 관련 키워드들
                    dev_keywords = ['python', 'javascript', 'java', 'react', 'node', 'developer', 'engineer', 'programmer', 'frontend', 'backend', 'full-stack', 'software', '개발자', '엔지니어', '프로그래머']
                    
                    if (term.lower() in position or 
                        term.lower() in company or
                        any(keyword in position for keyword in dev_keywords)):
                        jobs.append(jobs_detail(job_data))
            
            return jobs
        else:
            print(f"Can't get jobs. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []


def jobs_detail(job_data):
    """원티드 API 데이터에서 작업 정보 추출"""
    company = job_data.get('company', {}).get('name', 'N/A')
    position = job_data.get('position', 'N/A')
    
    # 위치 정보 추출
    location = job_data.get('address', {}).get('location', 'N/A')
    if location == 'N/A':
        location = job_data.get('address', {}).get('country', 'N/A')
    
    # 경력 정보
    experience = job_data.get('requirement', 'N/A')
    
    # 자격요건
    requirements = job_data.get('main_tasks', 'N/A')
    
    # 주요업무
    main_tasks = job_data.get('main_tasks', 'N/A')
    
    # 연봉 정보
    salary = job_data.get('annual_to', 'N/A')
    if salary and salary != 'N/A':
        salary = f"{salary}만원"
    
    # 링크 생성
    job_id = job_data.get('id', '')
    link = f"https://www.wanted.co.kr/wd/{job_id}" if job_id else ""
    
    return {
        'company': company,
        'position': position,
        'location': location,
        'experience': experience,
        'requirements': requirements,
        'main_tasks': main_tasks,
        'salary': salary,
        'link': link,
        'source': '원티드'
    }


def get_wanted_job(word):
    return extract_jobs(word)
