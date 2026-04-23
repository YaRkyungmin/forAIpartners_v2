from pages.ad_regist_page import estate_property_copy
from pages.menu_action import hover_and_click_ad_management
from pages.owner_regist_page import regist_owner_info
from utils.ad_regist_scheduler import should_register_today
from utils.property_mapper import *
from utils.sheet_driver import update_last_ad_regist_date, update_last_ad_cost_summary
from utils.sleep_manager import medium_sleep


def regist_ads_by_property(driver, sheet_row_number, property_info, owner_info, ad_schedule):
    # TODO: 광고갯수가 많아 졌을때는 끌올기능으로 하도록 해야함
    for _ in range(int(ad_schedule.num_of_ads)):
        # 광고 등록 페이지
        estate_property_copy(driver, property_info)

        # 소유자 등록 페이지
        regist_owner_info(driver, owner_info)

        # 최신 광고등록일 업데이트
        update_last_ad_regist_date(sheet_row_number)

        # 광고비 통계시트 업데이트
        update_last_ad_cost_summary()

        # 광고하기 페이지 클릭
        hover_and_click_ad_management(driver)
        medium_sleep()

def regist_valid_ad_value(driver, valid_ad_value):
    for row_number, value in enumerate(valid_ad_value):
        ad_schedule = map_ad_schedule_from_google_sheet(value)

        if not should_register_today(ad_schedule):
            continue

        property_info = map_property_info_from_google_sheet(value)
        owner_info = map_owner_info_from_google_sheet(value)

        # TODO: 모든 예외 처리 main까지 끌고와서 로깅을 하든지 통계 내기 전에 에러를 처리하든지 해야함

        regist_ads_by_property(
            driver=driver,
            sheet_row_number=row_number,
            property_info=property_info,
            owner_info=owner_info,
            ad_schedule=ad_schedule
        )