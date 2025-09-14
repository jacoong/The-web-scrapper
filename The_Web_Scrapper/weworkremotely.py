from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    """WeWorkRemotely에서 프로그래밍 관련 작업 검색"""
    # 프로그래밍 카테고리 페이지 사용
    url = "https://weworkremotely.com/categories/remote-programming-jobs"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            job_list = soup.find_all("li", "feature")
            
            jobs = []
            for job in job_list:
                job_detail = jobs_detail(job)
                # 프로그래밍 관련 키워드들로 필터링 완화
                programming_keywords = ['python', 'javascript', 'java', 'react', 'node', 'developer', 'engineer', 'programmer', 'frontend', 'backend', 'full-stack', 'software']
                
                # 검색어나 프로그래밍 키워드가 포함된 경우 포함
                if (term.lower() in job_detail['position'].lower() or 
                    term.lower() in job_detail['company'].lower() or
                    any(keyword in job_detail['position'].lower() for keyword in programming_keywords)):
                    jobs.append(job_detail)
            
            return jobs
        else:
            print(f"Can't get jobs. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []


def jobs_detail(job):
    """새로운 구조에서 작업 정보 추출"""
    try:
        # 회사명 추출 - 링크에서 추출
        company_link = job.find("a", href=lambda x: x and "/company/" in x)
        company = "N/A"
        if company_link:
            href = company_link.get('href', '')
            company = href.split('/company/')[-1].replace('-', ' ').title()
        
        # 포지션 추출 - h3 태그에서
        position_element = job.find("h3", "new-listing__header__title")
        position = position_element.text.strip() if position_element else "N/A"
        
        # 위치 추출 - 지역 정보 찾기
        location_element = job.find("span", class_=lambda x: x and "region" in x)
        if not location_element:
            # 다른 방법으로 위치 찾기
            location_div = job.find("div", class_=lambda x: x and "location" in x)
            if location_div:
                location_element = location_div.find("span")
        
        location = location_element.text.strip() if location_element else "Remote"
        
        # 링크 추출
        job_link = job.find("a", href=lambda x: x and "/remote-jobs/" in x)
        link = ""
        if job_link:
            href = job_link.get('href')
            if href:
                link = f"https://weworkremotely.com{href}"
        
        return {
            'company': company,
            'position': position,
            'location': location,
            'experience': 'N/A',
            'requirements': 'N/A',
            'main_tasks': 'N/A',
            'salary': 'N/A',
            'link': link,
            'source': 'WeWorkRemotely'
        }
    except Exception as e:
        print(f"Error parsing job details: {e}")
        return {
            'company': 'N/A',
            'position': 'N/A',
            'location': 'Remote',
            'experience': 'N/A',
            'requirements': 'N/A',
            'main_tasks': 'N/A',
            'salary': 'N/A',
            'link': '',
            'source': 'WeWorkRemotely'
        }


def get_weworkremotely_job(word):
    return extract_jobs(word)