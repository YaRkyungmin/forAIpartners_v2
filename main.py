#utils
from utils.ad_regist_manager import regist_valid_ad_value
from utils.sleep_manager import *
from utils.chrome_driver import create_driver
from utils.sheet_driver import *
#pages
from pages.login_page import *
from pages.menu_action import *
#dto
from dto.user_dto import UserInfo

if __name__ == '__main__':

    # 크롬 드라이버 생성
    ai_driver = create_driver(headless=False)

    # 이실장 사이트 열기
    ai_driver.get("https://www.aipartner.com") # 이실장 사이트 열기
    long_sleep()

    # 로그인 하기
    go_to_login_page(ai_driver)
    login_value = get_admin_from_google_sheet() # 구글 시트에서 가져오기
    user_info = UserInfo.map_from_values(login_value) # 사용자 정보 매핑
    login_to_site(ai_driver, user_info)
    long_sleep()

    # 메뉴 이동
    hover_and_click_ad_management(ai_driver)

    # 광고 올릴 매물 정보 가져오기
    valid_ad_value = get_valid_ad_information_from_google_sheet()

    # 광고 포스팅
    regist_valid_ad_value(ai_driver, valid_ad_value)
    long_sleep()

    print("광고 포스팅 완료~!!")

    ai_driver.quit()