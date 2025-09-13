import requests
from bs4 import BeautifulSoup


def extract_jobs(term):
    """사람인에서 채용공고 검색"""
    url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword={term}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.9,en;q=0.8',
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            job_list = soup.find_all('div', class_='item_recruit')
            
            jobs = []
            for job in job_list:
                job_detail = jobs_detail(job)
                if job_detail:  # 유효한 데이터가 있는 경우만 추가
                    jobs.append(job_detail)
            
            return jobs
        else:
            print(f"Can't get jobs. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []


def jobs_detail(job):
    """사람인 채용공고에서 작업 정보 추출"""
    try:
        # 회사명 - corp_name 클래스 사용 (strong 태그)
        company_elem = job.find('strong', class_='corp_name')
        if company_elem:
            # strong 태그 안의 a 태그에서 회사명 추출
            link_elem = company_elem.find('a')
            if link_elem:
                company = link_elem.get_text(strip=True)
            else:
                company = company_elem.get_text(strip=True)
        else:
            company = "N/A"
        
        # 포지션
        position_elem = job.find('h2', class_='job_tit')
        if position_elem:
            position_link = position_elem.find('a')
            position = position_link.get_text(strip=True) if position_link else "N/A"
        else:
            position = "N/A"
        
        # 위치/조건
        condition_elem = job.find('div', class_='job_condition')
        location = condition_elem.get_text(strip=True) if condition_elem else "N/A"
        
        # 링크
        link_elem = job.find('a', class_='data_layer')
        link = ""
        if link_elem:
            href = link_elem.get('href')
            if href:
                link = f"https://www.saramin.co.kr{href}"
        
        # 연봉
        salary_elem = job.find('div', class_='job_sal')
        salary = salary_elem.get_text(strip=True) if salary_elem else "협의"
        
        # 경력
        experience = "N/A"
        if condition_elem:
            condition_text = condition_elem.get_text(strip=True)
            if "신입" in condition_text:
                experience = "신입"
            elif "경력" in condition_text:
                experience = "경력"
        
        # 자격요건
        requirements_elem = job.find('div', class_='job_etc')
        requirements = requirements_elem.get_text(strip=True) if requirements_elem else "N/A"
        
        return {
            'company': company,
            'position': position,
            'location': location,
            'experience': experience,
            'requirements': requirements,
            'main_tasks': 'N/A',  # 사람인에서는 별도로 제공하지 않음
            'salary': salary,
            'link': link,
            'source': '사람인'
        }
    except Exception as e:
        print(f"Error parsing job details: {e}")
        return None


def get_saramin_job(word):
    return extract_jobs(word)
