
const index_submit_button = document.querySelector(".submit-button");
const index_loading_button = document.querySelector(".loading-button");

// 사이트 선택 기능
document.addEventListener('DOMContentLoaded', function() {
    const sourceItems = document.querySelectorAll('.source-item');
    const wantedInput = document.getElementById('wantedInput');
    const saraminInput = document.getElementById('saraminInput');
    const remoteokInput = document.getElementById('remoteokInput');
    const weworkremotelyInput = document.getElementById('weworkremotelyInput');
    
    // 지역 선택 기능
    const cityLevel = document.getElementById('cityLevel');
    const districtLevel = document.getElementById('districtLevel');
    const locationsInput = document.getElementById('locationsInput');
    const selectAllBtn = document.getElementById('selectAllLocations');
    const clearAllBtn = document.getElementById('clearAllLocations');
    
    // 지역 데이터
    const locationData = {
        '서울': ['강남구', '송파구', '서초구', '마포구', '용산구', '중구', '종로구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '강동구'],
        '경기': ['성남시', '수원시', '안양시', '안산시', '용인시', '부천시', '광명시', '평택시', '과천시', '오산시', '시흥시', '군포시', '의왕시', '하남시', '이천시', '안성시', '김포시', '화성시', '광주시', '여주시'],
        '인천': ['중구', '동구', '미추홀구', '연수구', '남동구', '부평구', '계양구', '서구', '강화군', '옹진군'],
        '부산': ['중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '강서구', '연제구', '수영구', '사상구', '기장군'],
        '대구': ['중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '달성군'],
        '대전': ['동구', '중구', '서구', '유성구', '대덕구'],
        '광주': ['동구', '서구', '남구', '북구', '광산구'],
        '울산': ['중구', '남구', '동구', '북구', '울주군'],
        '세종': ['세종시'],
        '강원': ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군'],
        '충북': ['청주시', '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군', '괴산군', '음성군', '단양군'],
        '충남': ['천안시', '공주시', '보령시', '아산시', '서산시', '논산시', '계룡시', '당진시', '금산군', '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군'],
        '전북': ['전주시', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군'],
        '전남': ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군'],
        '경북': ['포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군'],
        '경남': ['창원시', '진주시', '통영시', '사천시', '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군', '거창군', '합천군'],
        '제주': ['제주시', '서귀포시']
    };
    
    let selectedDistricts = new Set();
    
    // 각 사이트 아이템에 클릭 이벤트 추가
    sourceItems.forEach(item => {
        item.addEventListener('click', function() {
            const site = this.getAttribute('data-site');
            const isSelected = this.classList.contains('selected');
            
            // 최소 1개 사이트는 선택되어야 함
            const selectedCount = document.querySelectorAll('.source-item.selected').length;
            if (isSelected && selectedCount <= 1) {
                // 마지막 하나는 선택 해제할 수 없음
                return;
            }
            
            // 토글 기능
            if (isSelected) {
                this.classList.remove('selected');
                this.classList.add('disabled');
                // 해당 입력 필드 비활성화
                if (site === 'wanted') wantedInput.value = 'false';
                if (site === 'saramin') saraminInput.value = 'false';
                if (site === 'remoteok') remoteokInput.value = 'false';
                if (site === 'weworkremotely') weworkremotelyInput.value = 'false';
            } else {
                this.classList.add('selected');
                this.classList.remove('disabled');
                // 해당 입력 필드 활성화
                if (site === 'wanted') wantedInput.value = 'true';
                if (site === 'saramin') saraminInput.value = 'true';
                if (site === 'remoteok') remoteokInput.value = 'true';
                if (site === 'weworkremotely') weworkremotelyInput.value = 'true';
            }
        });
    });
    
    // 지역 선택 기능
    function updateLocationsInput() {
        locationsInput.value = Array.from(selectedDistricts).join(',');
    }
    
    function updateDistrictLevel(city) {
        districtLevel.innerHTML = '';
        
        if (locationData[city]) {
            locationData[city].forEach(district => {
                const item = document.createElement('span');
                item.className = 'location-item';
                item.setAttribute('data-district', district);
                item.textContent = district;
                
                if (selectedDistricts.has(district)) {
                    item.classList.add('selected');
                }
                
                item.addEventListener('click', function() {
                    if (this.classList.contains('selected')) {
                        this.classList.remove('selected');
                        selectedDistricts.delete(district);
                    } else {
                        this.classList.add('selected');
                        selectedDistricts.add(district);
                    }
                    updateLocationsInput();
                });
                
                districtLevel.appendChild(item);
            });
        }
    }
    
    // 시/도 선택 이벤트
    cityLevel.addEventListener('click', function(e) {
        if (e.target.classList.contains('location-item')) {
            const city = e.target.getAttribute('data-city');
            updateDistrictLevel(city);
        }
    });
    
    // 전체 선택 버튼
    selectAllBtn.addEventListener('click', function() {
        const allDistricts = document.querySelectorAll('#districtLevel .location-item');
        allDistricts.forEach(item => {
            item.classList.add('selected');
            selectedDistricts.add(item.getAttribute('data-district'));
        });
        updateLocationsInput();
    });
    
    // 전체 해제 버튼
    clearAllBtn.addEventListener('click', function() {
        const allDistricts = document.querySelectorAll('#districtLevel .location-item');
        allDistricts.forEach(item => {
            item.classList.remove('selected');
        });
        selectedDistricts.clear();
        updateLocationsInput();
    });
    
    // 폼 제출 전 검증
    const searchForm = document.getElementById('searchForm');
    searchForm.addEventListener('submit', function(e) {
        const selectedCount = document.querySelectorAll('.source-item.selected').length;
        if (selectedCount === 0) {
            e.preventDefault();
            alert('최소 1개 사이트를 선택해주세요!');
            return false;
        }
        
        // 지역 선택 검증 (선택사항)
        const selectedLocations = document.querySelectorAll('.location-item.selected').length;
        if (selectedLocations === 0) {
            if (!confirm('지역을 선택하지 않았습니다. 모든 지역에서 검색하시겠습니까?')) {
                e.preventDefault();
                return false;
            }
        }
        
        loading();
    });
});

function loading(){
    if (index_submit_button) {
    index_submit_button.classList.add("hidden");
    }
    if (index_loading_button) {
    index_loading_button.classList.remove("hidden");
    }
}

function main(){
    location.href = "/";
    if (index_submit_button) {
    index_submit_button.classList.remove("hidden");
    }
    if (index_loading_button) {
    index_loading_button.classList.add("hidden");
    }
}

function resetSearchButton(){
    // 검색 완료 후 버튼 상태 복원
    if (index_submit_button) {
        index_submit_button.classList.remove("hidden");
    }
    if (index_loading_button) {
        index_loading_button.classList.add("hidden");
    }
}

// 페이지 로드 시 검색 버튼 상태 복원
document.addEventListener('DOMContentLoaded', function() {
    resetSearchButton();
    
    // 모바일 터치 이벤트 최적화
    addMobileTouchEvents();
});

// 모바일 터치 이벤트 추가
function addMobileTouchEvents() {
    // 스크래퍼 아이템에 터치 이벤트 추가
    const scraperItems = document.querySelectorAll('.scraper-item');
    scraperItems.forEach(item => {
        item.addEventListener('touchstart', function(e) {
            e.preventDefault();
            this.style.transform = 'scale(0.95)';
        });
        
        item.addEventListener('touchend', function(e) {
            e.preventDefault();
            this.style.transform = 'scale(1)';
            // 클릭 이벤트 트리거
            this.click();
        });
        
        item.addEventListener('touchcancel', function(e) {
            e.preventDefault();
            this.style.transform = 'scale(1)';
        });
    });
    
    // 지역 아이템에 터치 이벤트 추가
    const locationItems = document.querySelectorAll('.location-item');
    locationItems.forEach(item => {
        item.addEventListener('touchstart', function(e) {
            e.preventDefault();
            this.style.transform = 'scale(0.95)';
        });
        
        item.addEventListener('touchend', function(e) {
            e.preventDefault();
            this.style.transform = 'scale(1)';
            // 클릭 이벤트 트리거
            this.click();
        });
        
        item.addEventListener('touchcancel', function(e) {
            e.preventDefault();
            this.style.transform = 'scale(1)';
        });
    });
    
    // 버튼에 터치 피드백 추가
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('touchstart', function(e) {
            this.style.transform = 'scale(0.95)';
            this.style.opacity = '0.8';
        });
        
        button.addEventListener('touchend', function(e) {
            this.style.transform = 'scale(1)';
            this.style.opacity = '1';
        });
        
        button.addEventListener('touchcancel', function(e) {
            this.style.transform = 'scale(1)';
            this.style.opacity = '1';
        });
    });
    
    // iOS Safari에서 줌 방지를 위한 메타 태그 확인
    const viewport = document.querySelector('meta[name="viewport"]');
    if (viewport) {
        viewport.setAttribute('content', 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no');
    }
}

