import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException

from dto.property_dto import PropertyInfo
from utils.ad_content_manipulator import generate_address_variations, generate_full_address, split_address_number
from utils.alert_handler import handle_alert
from utils.sleep_manager import *

def click_ad_regist_button(driver: WebDriver):
    try:
        ad_regist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="offeringsRegBtn"]'))
        )
        ad_regist_button.click()
    except TimeoutException:
        pass

def click_ad_load_button(driver: WebDriver):
    try:
        ad_regist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnBringId"))
        )
        ad_regist_button.click()
    except TimeoutException:
        pass

def open_dropdown(driver: WebDriver):
    try:
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "scAreaTitle"))
        )
        dropdown_button.click()
    except TimeoutException:
        pass

def click_dropdown_item(driver: WebDriver, category: str, location: str):
    target_text = f"{category}>{location}"
    try:
        area_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="scAreaSelect"]//a'))
        )

        for index, item in enumerate(area_list, start=1):
            if target_text in item.text:
                target_xpath = f'//*[@id="scAreaSelect"]/a[{index}]'
                clickable_item = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, target_xpath))
                )
                clickable_item.click()
                return

        print(f"'{target_text}' 텍스트를 가진 항목을 찾지 못했습니다.")

    except TimeoutException:
        print("지역 선택 항목 로딩에 실패했습니다.")

def prepare_listing_by_deal_type_and_address(driver: WebDriver, deal_type: str, address: str):
    try:
        # 드롭다운 버튼 클릭
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='scOfferTitle']"))
        )
        dropdown.click()

        deal_xpath_map = {
            "매매": "//*[@id='scOfferSelect']/a[2]",
            "전세": "//*[@id='scOfferSelect']/a[3]",
            "월세": "//*[@id='scOfferSelect']/a[4]",
            "단기": "//*[@id='scOfferSelect']/a[5]"
        }

        # 거래유형 체크
        item_xpath = deal_xpath_map.get(deal_type)
        if not item_xpath:
            raise ValueError(f"지원하지 않는 거래유형입니다: {deal_type}")

        # 거래유형 항목 선택
        deal_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        deal_item.click()
        short_sleep()

        # 기존 매물 데이터 확인
        old_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="importListArea"]/tr[1]'))
        )

        # 주소지 입력
        enter_address_number(driver, address)
        short_sleep()

        # 불러오기 버튼 클릭
        ad_import_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btnImport.GTM_offerings_ad_list_regbtn_load_lo"))
        )
        ad_import_button.click()
        short_sleep()

        # 새로운 매물 데이터 업로드 됐는지 확인
        if old_element:
            WebDriverWait(driver, 3).until(EC.staleness_of(old_element))

    except TimeoutException:
        print(f"{deal_type} 항목 또는 버튼을 클릭하는 데 실패했습니다.")

def enter_address_number(driver: WebDriver, address: str):
    try:
        main, sub = split_address_number(address)

        house_no1_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "houseNo1"))
        )
        driver.execute_script("arguments[0].value = arguments[1];", house_no1_input, main)
        short_sleep()

        house_no2_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "houseNo2"))
        )
        driver.execute_script("arguments[0].value = arguments[1];", house_no2_input, sub)
        short_sleep()

    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def click_radio_button(driver: WebDriver, location: str, house_number: str, dong_number: str, room_number: str):
    # TODO: 전세가 혹은 월세가 가 달라졌을때 예외처리를 해야함 인자를 전세보증금, 월세보증금, 월세 이렇게 세개를 받아서 비교해야함
    #   "leasePrc":39600,
    #     "depositPrc":0,
    #     "monthlyPrc":0,
    try:
        radio_inputs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.NAME, "saleSelect0"))
        )
        target_address = [location, house_number, room_number]

        if dong_number != "-":
            target_address.insert(2, f"{dong_number}동")

        for radio_input in radio_inputs:
            value = radio_input.get_attribute('value')

            try:
                value_json = json.loads(value)
            except json.JSONDecodeError:
                continue

            addr_str = value_json.get('addrStr', '')

            if all(item in addr_str for item in target_address):
                radio_id = radio_input.get_attribute('id')
                label_xpath = f"//label[@for='{radio_id}']"
                label = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, label_xpath))
                )
                driver.execute_script("arguments[0].click();", label)

                WebDriverWait(driver, 5).until(
                    lambda d: d.find_element(By.ID, radio_id).is_selected()
                )

                return

    # TODO: 여기까지 코드 흐름이 왔으면 주소가 잘못됐다는 에러를 던져야함

    except TimeoutException:
        print("라디오 버튼을 찾는 데 실패했습니다.")

def click_copy_button(driver: WebDriver):
    try:
        copy_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btnCopy.GTM_offerings_ad_list_regbtn_load_copy")
            )
        )
        copy_button.click()
    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def check_address(driver: WebDriver, dong_number: str, floor_number: str, room_number: str):
    address_variations = generate_address_variations(dong_number, floor_number, room_number)

    for address in address_variations:
        try:
            detail_addr_input = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='detailAddr']"))
            )
        except TimeoutException:
            print("detailAddr 요소가 10초 내에 나타나지 않았습니다.")
            continue

        # 매물주소입력 창 없애기
        detail_addr_input.clear()
        short_sleep()

        # 새로운 주소로 주소입력 창 채우기
        detail_addr_input.send_keys(address)
        short_sleep()

        try:
            address_confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@class,'btn-address-confirm') and contains(text(),'주소확인')]")
                )
            )
            address_confirm_button.click()
        except TimeoutException:
            print("주소 확인 버튼을 찾을 수 없습니다.")
            continue

        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//td//i[contains(@class, 'ico-confirmed')]"))
            )

            message_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@id='address-confirm-pop-same-offerings']//td"))
            )
            message_text = message_element.text.strip()

            # 주소확인 팝업 찾기
            popup = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH, "//div[@class='popup-header'][.//p[text()='주소 확인']]"
                ))
            )

            # 팝업 안의 닫기 버튼
            close_button = popup.find_element(By.CSS_SELECTOR, "a.close")
            close_button.click()

            if "동일주소 매물 존재" not in message_text:
                break

        except TimeoutException:
            print(f"주소 확인 실패: {address}")

def check_room_type(driver: WebDriver, room_type: str):
    try:
        room_cnt_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "setRoomCnt"))
        )
        room_count = room_cnt_elem.get_attribute("value")

        if room_count != "1":
            return

        if room_type == "open":
            target_selector = "label[for='setStructGbn1']"
        elif room_type == "sep":
            target_selector = "label[for='setStructGbn2']"
        else:
            return

        target = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, target_selector))
        )
        target.click()

    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def reorder_images_random(driver: WebDriver):
    try:
        img_items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.imgItem'))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.imgItem.ui-sortable-handle'))
        )

        from_img = img_items[0]
        to_img = img_items[1]

        action = ActionChains(driver)
        action.click_and_hold(from_img).move_to_element(to_img).release().perform()

    except TimeoutException:
        pass


def click_ad_publish_button(driver: WebDriver):
    try:
        # 광고하기 버튼
        ad_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btnConfirm.GTM_offerings_ad_list_regbtn_ad")
            )
        )
        ad_button.click()
        short_sleep()

        # 얼럿 광고 확인 버튼
        handle_alert(driver)

    except TimeoutException:
        pass

def estate_property_copy(driver: WebDriver, property: PropertyInfo):
    # 광고등록 버튼
    click_ad_regist_button(driver)
    short_sleep()

    # 매물불러오기 버튼
    click_ad_load_button(driver)
    short_sleep()

    # 드롭다운 내리기
    open_dropdown(driver)
    short_sleep()

    if property.building_type == "vil":
        # 매물 찾기
        full_address = generate_full_address(property.city_name, property.district_name, property.dong_name)
        click_dropdown_item(driver, "빌라/연립", full_address)
        short_sleep()

        # 거래방식 과 주소지로 매물 불러오기
        prepare_listing_by_deal_type_and_address(driver, property.deal_type, property.address)
        short_sleep()

        # 복사할 매물 선택 버튼 클릭
        click_radio_button(driver, property.dong_name, property.address, property.dong_number, property.room_number)
        short_sleep()

        #TODO: 전세가 혹은 월세가 가 달라졌을때 예외처리를 해줘야함

        # 복사 버튼
        click_copy_button(driver)
        short_sleep()

        # 동일 주소 검증
        check_address(driver, property.dong_number, property.floor_number, property.room_number)
        short_sleep()

        # 방구조 선택
        check_room_type(driver, property.room_type)
        short_sleep()

        #TODO: 복층형 타입 일떄 처리

        # 광고 등록 버튼 및 얼럿 처리
        click_ad_publish_button(driver)

        #TODO: 중복광고 예외처리 해야함 얼럿 메세지 읽어서 비교해주는 예외처리 필요
    elif property.building_type == "op":
         # TODO: 오피스텔 일 때
         print("TODO")