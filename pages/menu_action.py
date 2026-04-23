from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

def hover_and_click_ad_management(driver: WebDriver):
    hover_and_click(driver, "GTM_offerings")

def hover_and_click(driver: WebDriver, element_class_name: str):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, element_class_name))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except (ElementClickInterceptedException, NoSuchElementException, TimeoutException) as e:
        print(f"Error: {e}")