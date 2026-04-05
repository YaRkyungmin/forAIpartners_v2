from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dto.user_dto import UserInfo


def go_to_login_page(driver: WebDriver):
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.GTM_non_login_main_login"))
    )
    login_button.click()

def login_to_site(driver: WebDriver, user: UserInfo):
    id_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "member-id"))
    )
    id_input.send_keys(user.id)

    pw_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "member-pw"))
    )
    pw_input.send_keys(user.password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-login"))
    )
    login_button.click()