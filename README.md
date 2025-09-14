# Job Scrapper - 채용 정보 검색 시스템

한국의 주요 채용사이트에서 채용공고를 검색하고 필터링할 수 있는 웹 애플리케이션입니다.

## 🚀 기능

- **다중 사이트 검색**: 원티드, 사람인, 잡플래닛, 워크넷
- **지역별 필터링**: 시/도 → 구/군 계층적 선택
- **사이트별 필터링**: 검색 결과에서 특정 사이트만 표시
- **CSV 다운로드**: 검색 결과를 CSV 파일로 내보내기
- **반응형 디자인**: 모바일/데스크톱 최적화

## 📊 지원 사이트

- **원티드**: 실제 API 데이터
- **사람인**: 실제 스크래핑 데이터  
- **잡플래닛**: 현실적인 더미 데이터 (IT 대기업)
- **워크넷**: 현실적인 더미 데이터 (공공기관/대기업)

## 🛠️ 기술 스택

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Web Scraping**: requests, BeautifulSoup
- **Deployment**: Render (무료)

## 📦 설치 및 실행

### 로컬 실행
```bash
# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate     # Windows

# 의존성 설치
pip install -r requirements.txt

# 앱 실행
cd The_Web_Scrapper
python3 frontend_.py
```

### 배포 (Render)
1. GitHub에 코드 업로드
2. Render.com에서 새 Web Service 생성
3. GitHub 저장소 연결
4. 자동 배포 완료

## 🌐 사용법

1. 검색어 입력 (예: "python", "파이썬", "개발자")
2. 검색할 사이트 선택 (원티드, 사람인, 잡플래닛, 워크넷)
3. 지역 선택 (선택사항)
4. 검색 실행
5. 결과 필터링 및 CSV 다운로드

## 📝 라이선스

MIT License