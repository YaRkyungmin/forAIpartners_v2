from selenium import webdriver

def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.



if __name__ == '__main__':

    driver = webdriver.Chrome()

    print(driver.capabilities['browserVersion'])
    print(driver.capabilities['chrome']['chromedriverVersion'])

    driver.quit()

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조