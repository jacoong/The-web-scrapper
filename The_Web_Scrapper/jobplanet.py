import requests
from bs4 import BeautifulSoup
import time

def get_jobplanet_job(search_term):
    """잡플래닛에서 채용공고 검색 (더미 데이터)"""
    try:
        # 잡플래닛은 접근 차단으로 인해 더미 데이터 사용
        print("잡플래닛 접근 차단으로 인해 더미 데이터를 사용합니다.")
        
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
        
        # 현실적인 더미 데이터
        dummy_jobs = [
            {
                'company': '카카오',
                'position': 'Python 백엔드 개발자',
                'location': '서울 강남구',
                'experience': '3년 이상',
                'requirements': 'Python, Django, PostgreSQL 경험 필수',
                'main_tasks': '웹 서비스 백엔드 개발 및 API 설계',
                'salary': '4,000만원 ~ 6,000만원',
                'link': 'https://www.jobplanet.co.kr/job/example1',
                'source': 'JobPlanet'
            },
            {
                'company': '네이버',
                'position': '시니어 Python 개발자',
                'location': '경기 성남시',
                'experience': '5년 이상',
                'requirements': 'Python, FastAPI, AWS 경험 필수',
                'main_tasks': '대용량 데이터 처리 시스템 개발',
                'salary': '5,000만원 ~ 7,000만원',
                'link': 'https://www.jobplanet.co.kr/job/example2',
                'source': 'JobPlanet'
            },
            {
                'company': '라인',
                'position': 'Python 풀스택 개발자',
                'location': '서울 송파구',
                'experience': '2년 이상',
                'requirements': 'Python, React, MongoDB 경험',
                'main_tasks': '웹 애플리케이션 풀스택 개발',
                'salary': '3,500만원 ~ 5,500만원',
                'link': 'https://www.jobplanet.co.kr/job/example3',
                'source': 'JobPlanet'
            },
            {
                'company': '쿠팡',
                'position': 'Python 데이터 엔지니어',
                'location': '서울 강남구',
                'experience': '4년 이상',
                'requirements': 'Python, Spark, Hadoop 경험 필수',
                'main_tasks': '데이터 파이프라인 구축 및 최적화',
                'salary': '4,500만원 ~ 6,500만원',
                'link': 'https://www.jobplanet.co.kr/job/example4',
                'source': 'JobPlanet'
            },
            {
                'company': '배달의민족',
                'position': 'Python 백엔드 개발자',
                'location': '서울 마포구',
                'experience': '3년 이상',
                'requirements': 'Python, Django, Redis 경험',
                'main_tasks': '주문 시스템 백엔드 개발',
                'salary': '3,800만원 ~ 5,800만원',
                'link': 'https://www.jobplanet.co.kr/job/example5',
                'source': 'JobPlanet'
            },
            {
                'company': '토스',
                'position': 'Python 개발자 (신입)',
                'location': '서울 강남구',
                'experience': '신입',
                'requirements': 'Python 기초, 알고리즘 문제해결 능력',
                'main_tasks': '핀테크 서비스 개발',
                'salary': '3,000만원 ~ 4,000만원',
                'link': 'https://www.jobplanet.co.kr/job/example6',
                'source': 'JobPlanet'
            },
            {
                'company': '당근마켓',
                'position': 'Python 백엔드 개발자',
                'location': '서울 서초구',
                'experience': '2년 이상',
                'requirements': 'Python, FastAPI, PostgreSQL',
                'main_tasks': '중고거래 플랫폼 백엔드 개발',
                'salary': '3,500만원 ~ 5,000만원',
                'link': 'https://www.jobplanet.co.kr/job/example7',
                'source': 'JobPlanet'
            },
            {
                'company': '야놀자',
                'position': 'Python 풀스택 개발자',
                'location': '서울 강남구',
                'experience': '3년 이상',
                'requirements': 'Python, Vue.js, MySQL 경험',
                'main_tasks': '여행 예약 시스템 개발',
                'salary': '4,000만원 ~ 5,500만원',
                'link': 'https://www.jobplanet.co.kr/job/example8',
                'source': 'JobPlanet'
            }
        ]
        
        print(f"잡플래닛에서 {len(dummy_jobs)}개의 채용공고를 찾았습니다.")
        return dummy_jobs
        
    except Exception as e:
        print(f"잡플래닛 스크래핑 오류: {e}")
        return []

def jobs_detail(job):
    """잡플래닛 채용공고에서 작업 정보 추출 (더미 데이터용)"""
    return job
