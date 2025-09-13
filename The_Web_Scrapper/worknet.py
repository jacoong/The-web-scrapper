import requests
from bs4 import BeautifulSoup
import time

def get_worknet_job(search_term):
    """워크넷에서 채용공고 검색 (더미 데이터)"""
    try:
        # 워크넷은 접근 차단으로 인해 더미 데이터 사용
        print("워크넷 접근 차단으로 인해 더미 데이터를 사용합니다.")
        
        # 한국어/영어 키워드 매핑
        korean_keywords = {
            'python': ['파이썬', 'python', '개발자', '프로그래머'],
            'java': ['자바', 'java', '개발자', '프로그래머'],
            'javascript': ['자바스크립트', 'javascript', 'js', '개발자'],
            'react': ['리액트', 'react', '프론트엔드', '개발자'],
            'spring': ['스프링', 'spring', '백엔드', '개발자'],
            '개발자': ['개발자', '프로그래머', '엔지니어', 'developer'],
            '프로그래머': ['프로그래머', '개발자', '엔지니어', 'programmer']
        }
        
        # 검색어가 키워드에 포함되는지 확인
        search_lower = search_term.lower()
        is_relevant = False
        
        for keyword, variations in korean_keywords.items():
            if any(var in search_lower for var in variations):
                is_relevant = True
                break
        
        if not is_relevant:
            return []
        
        # 현실적인 더미 데이터 (공공기관/대기업 중심)
        dummy_jobs = [
            {
                'company': '한국전력공사',
                'position': 'Python 개발자',
                'location': '경기 성남시',
                'experience': '3년 이상',
                'requirements': 'Python, Django, Oracle DB 경험',
                'main_tasks': '전력 관리 시스템 개발',
                'salary': '3,500만원 ~ 5,000만원',
                'link': 'https://www.work.go.kr/job/example1',
                'source': 'WorkNet'
            },
            {
                'company': '한국가스공사',
                'position': '시니어 Python 개발자',
                'location': '서울 강남구',
                'experience': '5년 이상',
                'requirements': 'Python, FastAPI, PostgreSQL 경험 필수',
                'main_tasks': '가스 공급 시스템 백엔드 개발',
                'salary': '4,000만원 ~ 6,000만원',
                'link': 'https://www.work.go.kr/job/example2',
                'source': 'WorkNet'
            },
            {
                'company': '한국수출입은행',
                'position': 'Python 풀스택 개발자',
                'location': '서울 중구',
                'experience': '2년 이상',
                'requirements': 'Python, React, MySQL 경험',
                'main_tasks': '금융 시스템 웹 애플리케이션 개발',
                'salary': '3,800만원 ~ 5,500만원',
                'link': 'https://www.work.go.kr/job/example3',
                'source': 'WorkNet'
            },
            {
                'company': '한국산업은행',
                'position': 'Python 데이터 분석가',
                'location': '서울 영등포구',
                'experience': '4년 이상',
                'requirements': 'Python, Pandas, NumPy, SQL 경험 필수',
                'main_tasks': '금융 데이터 분석 및 모델링',
                'salary': '4,200만원 ~ 6,200만원',
                'link': 'https://www.work.go.kr/job/example4',
                'source': 'WorkNet'
            },
            {
                'company': '한국토지주택공사',
                'position': 'Python 백엔드 개발자',
                'location': '경기 성남시',
                'experience': '3년 이상',
                'requirements': 'Python, Django, Redis 경험',
                'main_tasks': '부동산 관리 시스템 개발',
                'salary': '3,600만원 ~ 5,200만원',
                'link': 'https://www.work.go.kr/job/example5',
                'source': 'WorkNet'
            },
            {
                'company': '한국도로공사',
                'position': 'Python 개발자 (신입)',
                'location': '경기 성남시',
                'experience': '신입',
                'requirements': 'Python 기초, 알고리즘 문제해결 능력',
                'main_tasks': '도로 관리 시스템 개발',
                'salary': '3,000만원 ~ 4,200만원',
                'link': 'https://www.work.go.kr/job/example6',
                'source': 'WorkNet'
            },
            {
                'company': '한국철도공사',
                'position': 'Python 시스템 개발자',
                'location': '서울 용산구',
                'experience': '4년 이상',
                'requirements': 'Python, FastAPI, MongoDB',
                'main_tasks': '철도 운영 시스템 개발',
                'salary': '4,000만원 ~ 5,800만원',
                'link': 'https://www.work.go.kr/job/example7',
                'source': 'WorkNet'
            },
            {
                'company': '한국공항공사',
                'position': 'Python 풀스택 개발자',
                'location': '인천 중구',
                'experience': '3년 이상',
                'requirements': 'Python, Vue.js, PostgreSQL 경험',
                'main_tasks': '공항 운영 시스템 개발',
                'salary': '3,700만원 ~ 5,300만원',
                'link': 'https://www.work.go.kr/job/example8',
                'source': 'WorkNet'
            }
        ]
        
        print(f"워크넷에서 {len(dummy_jobs)}개의 채용공고를 찾았습니다.")
        return dummy_jobs
        
    except Exception as e:
        print(f"워크넷 스크래핑 오류: {e}")
        return []

def jobs_detail(job):
    """워크넷 채용공고에서 작업 정보 추출 (더미 데이터용)"""
    return job
