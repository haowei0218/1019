from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

screenshot_list = []


def screenshot_photo(driver, filename):
    try:
        driver.get_screenshot_as_file(filename)
        screenshot_list.append(filename)
    except Exception as e:
        print(f"Can't take Screenshot: {e}")


def click_class(wait, by, vaule):
    try:
        element = wait.until(EC.element_to_be_clickable((By, vaule)))
        element.click()
        time.sleep(3)
        return element
    except Exception as Error:
        print(f"Element Error{Error}")


try:
    # 開啟官網 使用手機模式
    mobile = {"deviceName": "iPhone 6/7/8"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile)
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(390, 844)
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    time.sleep(10)

    website = "官網首頁.png"
    driver.get_screenshot_as_file(website)

    # 創建一個函數 定位到元素並且點擊

    # 選單
    click_class(10, By.CLASS_NAME, "cubre-o-header__burger")
    p_info = "產品介紹.png"
    driver.get_screenshot_as_file(p_info)

    # 產品介紹
    wait = WebDriverWait(driver, 20)
    nav_content = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cubre-o-nav__content")))
    menu = nav_content.find_element(By.CLASS_NAME, "cubre-o-menu__item")
    menuSortBtn = menu.find_element(By.CLASS_NAME, "cubre-a-menuSortBtn.-l1")
    menuSortBtn.click()
    time.sleep(3)

    # 信用卡
    click_class(wait, By.CSS_SELECTOR, ".cubre-o-menuLinkList__btn .cubre-a-menuSortBtn")
    credit = "信用卡.png"
    driver.get_screenshot_as_file(credit)
    time.sleep(3)

    # 信用卡介紹
    click_class(wait, By.XPATH, '//*[@id="lnk_Link"]')
    credit_info = "信用卡介紹.png"
    driver.get_screenshot_as_file(credit_info)

    # 停發卡介面
    click_class(wait, By.CLASS_NAME, "cubre-m-anchor__wrap")
    stop_card = "停發卡介面.png"
    driver.get_screenshot_as_file(stop_card)

    # 向右滾動介面
    actions = ActionChains(driver)
    x_offset = 900
    driver.execute_script("window.scrollBy(300, 0)")
    time.sleep(2)

    # 對每個停發的卡進行點擊
    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[1]")
    screenshot_photo(driver, "停發卡1")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[2]")
    screenshot_photo(driver, "停發卡2")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[3]")
    screenshot_photo(driver, "停發卡3")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[4]")
    screenshot_photo(driver, "停發卡4")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[5]")
    screenshot_photo(driver, "停發卡5")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[6]")
    screenshot_photo(driver, "停發卡6")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[7]")
    screenshot_photo(driver, "停發卡7")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[8]")
    screenshot_photo(driver, "停發卡8")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[9]")
    screenshot_photo(driver, "停發卡9")

    click_class(wait, By.XPATH, "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[10]")
    screenshot_photo(driver, "停發卡10")

    driver.close()
except Exception as element_error:
    print(f"element_error{element_error}")
# 計算截圖
finally:
    count = len(screenshot_list)
    print(count)
    sys.exit()

