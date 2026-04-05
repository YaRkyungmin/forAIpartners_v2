from utils.chrome_driver import create_driver
from utils.sleep_manager import *

if __name__ == '__main__':

    ai_driver = create_driver(headless=False) # 크롬 드라이버 생성
    ai_driver.get("https://www.aipartner.com") # 이실장 사이트 열기
    long_sleep()

    ai_driver.quit()

