from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(headless: bool = False) -> webdriver.Chrome:  # 크롬 드라이버를 생성해서 반환하는 함수
    chrome_options = Options()

    if headless: # 창 없는 모드
        chrome_options.add_argument("--headless=new") # 최신 headless 모드 활성화
        chrome_options.add_argument("--disable-gpu") # GPU 사용 비활성화

    chrome_options.add_argument("--window-size=1920,1080") # 브라우저 창 크기를 1920x1080으로 고정

    chrome_options.add_argument("--disable-blink-features=AutomationControlled") # 자동화 브라우저 탐지 기능 비활성화
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 자동화 제어 문구 및 관련 설정 제거
    chrome_options.add_experimental_option("useAutomationExtension", False) # 자동화 확장 기능 비활성화

    chrome_options.add_argument("lang=ko_KR") # 브라우저 언어를 한국어로 설정

    chrome_options.add_argument(r"--user-data-dir=C:\Users\kkgm94\PycharmProjects\aipartner_v2\chrome_profile") # 크롬 브라우저 사용자 프로필 저장 경로 지정
    chrome_options.add_argument(r"--profile-directory=Default") # 어떤 프로필로 사용할 건지 지정

    prefs = { # 크롬 환경설정 딕셔너리 생성
        "profile.default_content_setting_values.notifications": 2 # 웹사이트 알림 팝업 차단
    }

    chrome_options.add_experimental_option("prefs", prefs) # 위 환경설정을 크롬 옵션에 적용

    driver = webdriver.Chrome(options=chrome_options) # 설정한 옵션으로 크롬 드라이버 실행

    driver.execute_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """)

    driver.execute_script("""
        Object.defineProperty(navigator, 'languages', {
            get: () => ['ko-KR', 'ko']
        });

        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3]
        });

        window.chrome = {
            runtime: {}
        };
    """)

    return driver