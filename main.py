#utils
from utils.sleep_manager import *
from utils.chrome_driver import create_driver
from utils.sheet_driver import get_admin_from_google_sheet
#pages
from pages.login_page import go_to_login_page, login_to_site
#dto
from dto.user_dto import UserInfo

if __name__ == '__main__':

    # 이실장 사이트 열기
    ai_driver = create_driver(headless=False) # 크롬 드라이버 생성
    ai_driver.get("https://www.aipartner.com") # 이실장 사이트 열기
    long_sleep()

    # 로그인 하기
    go_to_login_page(ai_driver)
    login_value = get_admin_from_google_sheet() # 시트에서 가져오기
    user_info = UserInfo.map_from_values(login_value)
    login_to_site(ai_driver, user_info)
    long_sleep()

    ai_driver.quit()