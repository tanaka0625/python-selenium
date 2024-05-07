from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time


options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://selenium:4444/wd/hub',
             options = options
             )

url = 'https://www.google.co.jp/' # テストでアクセスするURLを指定
driver.get(url)

driver.implicitly_wait(5) # 引数には時間を入れる

try:

    # 検索ボックスにpythonを入力
    search_bar = driver.find_element(By.ID, "APjFqb")
    # print(search_bar)
    search_bar.send_keys("python")

    # 検索
    search_bar.submit()

    time.sleep(5)

    driver.quit()

except NoSuchElementException as e:
    print("miss")
    print("")
    print(e)
    driver.quit()