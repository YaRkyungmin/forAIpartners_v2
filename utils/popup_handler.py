from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def close_aipartner_popup(driver, popup_id: int):
    try:
        close_button_xpath = f"//*[@id='aipartner-popup-layout-{popup_id}']/div/div[2]/div[2]/div/label"

        close_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, close_button_xpath))
        )

        close_button.click()

    except TimeoutException:
        print(f"닫기 버튼을 찾는 데 실패했습니다. popup_id: {popup_id}")

def close_aipartner_new_popup(driver):
    try:
        confirm_button_xpath = "/html/body/div[9]/div/div[3]/div[2]/a[1]"

        confirm_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, confirm_button_xpath))
        )

        confirm_button.click()

    except TimeoutException:
        print("확인 버튼을 찾는 데 실패했습니다.")