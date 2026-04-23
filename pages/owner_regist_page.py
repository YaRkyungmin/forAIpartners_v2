from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException

from dto.owner_dto import OwnerInfo
from utils.ad_content_manipulator import split_phone_number
from utils.alert_handler import handle_alert
from utils.sleep_manager import short_sleep
from dotenv import load_dotenv
import os

load_dotenv()

def click_verify_label(driver: WebDriver, verify_type: str):
    try:
        if "roc" in verify_type:
            label = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[@for='verifyType2']"))
            )
            label.click()
        elif "nav" in verify_type:
            label = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[@for='verifyType7']"))
            )
            label.click()
    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def enter_owner_name(driver: WebDriver, owner_name: str):
    try:
        owner_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='inputOname']"))
        )

        owner_name_input.clear()
        owner_name_input.send_keys(owner_name)

    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def select_telecom(driver: WebDriver, telecom_name: str):
    try:
        select_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='selectTelecom']"))
        )
        select_button.click()

        telecom_item_xpath = ""
        if telecom_name == "SKT":
            telecom_item_xpath = "//a[@data-value='01' and text()='SKT']"
        elif telecom_name == "KT":
            telecom_item_xpath = "//a[@data-value='02' and text()='KT']"
        elif telecom_name == "LGU+":
            telecom_item_xpath = "//a[@data-value='03' and text()='LGU+']"
        elif telecom_name == "SKT 알뜰폰":
            telecom_item_xpath = "//a[@data-value='04' and text()='SKT 알뜰폰']"
        elif telecom_name == "KT 알뜰폰":
            telecom_item_xpath = "//a[@data-value='05' and text()='KT 알뜰폰']"
        elif telecom_name == "LGU+ 알뜰폰":
            telecom_item_xpath = "//a[@data-value='06' and text()='LGU+ 알뜰폰']"

        telecom_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, telecom_item_xpath))
        )
        telecom_item.click()


    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def select_phone_number(driver: WebDriver, phone_number: str):
    try:
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="selectOphone1"]'))
        )
        dropdown_button.click()

        phone_010 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-num='010']"))
        )
        phone_010.click()

        first_part, second_part = split_phone_number(phone_number)

        first_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='phoneOphone2']"))
        )
        driver.execute_script("arguments[0].value = arguments[1];", first_input, first_part)

        second_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='phoneOphone3']"))
        )
        driver.execute_script("arguments[0].value = arguments[1];", second_input, second_part)

    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def select_gender(driver: WebDriver, gender: str):
    try:
        gender_xpath = ""
        if gender == "MAN":
            gender_xpath = "//label[@for='inputOsex1' and text()='남']"
        elif gender == "WOMAN":
            gender_xpath = "//label[@for='inputOsex2' and text()='여']"

        gender_label = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, gender_xpath))
        )
        gender_label.click()
    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def click_rocket_checkboxes(driver: WebDriver):
    try:
        consent_mobile_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='consentMobile2']"))
        )
        consent_mobile_checkbox.click()

        consent_required_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='consentRequired']"))
        )
        consent_required_checkbox.click()

    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def click_payment_button(driver: WebDriver):
    try:
        payment_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "naverSendSave"))
        )
        payment_button.click()

        handle_alert(driver)

    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")


def select_owner_type(driver: WebDriver, owner_type: str):
    try:
        if owner_type == "per":
            owner_type_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='divOwnerType1']/label"))
            )
            owner_type_button.click()
            short_sleep()
        elif owner_type == "cor":
            owner_type_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='divOwnerType2']/label"))
            )
            owner_type_button.click()
            short_sleep()
    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException) as e:
        print(f"Error: {e}")

def select_client_type(driver: WebDriver, owner_type: str):
    try:
        if owner_type == "per":
            client_type_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='divClientType1']/label"))
            )
            client_type_button.click()
        elif owner_type == "cor":
            client_type_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='divClientType4']/label"))
            )
            client_type_button.click()

    except (ElementClickInterceptedException, TimeoutException, NoSuchElementException) as e:
        print(f"Error: {e}")

def enter_owner_name_with_client(driver: WebDriver, owner_name: str, owner_type: str, client_name: str):
    try:
        if owner_type == "per":
            owner_name_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="inputName"]'))
            )
            owner_name_input.clear()
            short_sleep()

            owner_name_input.send_keys(owner_name)
            short_sleep()
        elif owner_type == "cor":
            owner_name_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="inputOname"]'))
            )
            owner_name_input.clear()
            short_sleep()

            owner_name_input.send_keys(owner_name)
            short_sleep()

            client_name_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="inputName"]'))
            )
            client_name_input.clear()
            short_sleep()

            client_name_input.send_keys(client_name)
    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")
def select_nav_phone_number(driver: WebDriver, phone_number: str):
    try:
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="selectCphone"]'))
        )
        dropdown_button.click()

        phone_010 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="item-cphone"]/a[2]'))
        )
        phone_010.click()
        short_sleep()

        first_part, second_part = split_phone_number(phone_number)

        first_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="phoneCphone2"]'))
        )
        driver.execute_script("arguments[0].value = arguments[1];", first_input, first_part)
        short_sleep()

        second_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="phoneCphone3"]'))
        )
        driver.execute_script("arguments[0].value = arguments[1];", second_input, second_part)
        short_sleep()
    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def upload_business_card(driver: WebDriver, owner_name: str, owner_type: str):
    if owner_type == "per":
        return

    try:
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fileReferenceFileUrl1"))
        )

        base_path = os.getenv("BUSINESS_CARD_PATH")
        file_path = os.path.join(base_path, f"{owner_name}.png")

        file_input.send_keys(file_path)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#tdReferenceFileUrl1Files ul li"))
        )

    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def click_nav_checkboxes(driver: WebDriver):
    try:
        checkbox_label = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "label[for='consentRequired']")
            )
        )
        checkbox_label.click()
    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")

def regist_owner_info(driver: WebDriver, owner_info: OwnerInfo):
    # 검증방식 선택
    click_verify_label(driver, owner_info.verify_type)
    short_sleep()

    if owner_info.verify_type == "roc":
        enter_owner_name(driver, owner_info.owner_name)
        select_telecom(driver, owner_info.telecom_name)
        select_phone_number(driver, owner_info.phone_number)
        select_gender(driver, owner_info.gender)
        click_rocket_checkboxes(driver)

    elif owner_info.verify_type == "nav":
        select_owner_type(driver, owner_info.owner_type)
        select_client_type(driver, owner_info.owner_type)
        enter_owner_name_with_client(driver, owner_info.owner_name, owner_info.owner_type, owner_info.client_name)
        select_nav_phone_number(driver, owner_info.phone_number)
        upload_business_card(driver, owner_info.owner_name, owner_info.owner_type)
        click_nav_checkboxes(driver)

    short_sleep()
    click_payment_button(driver)

    # TODO: 돈없을 때 예외 처리