from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time


options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://selenium:4444/wd/hub',
             options = options
             )

# try:

#     # url = 'https://www.google.co.jp/' # テストでアクセスするURLを指定
#     url = 'https://www.yahoo.co.jp/' # テストでアクセスするURLを指定
#     driver.get(url)

#     driver.implicitly_wait(5) # 引数には時間を入れる

#     driver.quit()

# except NoSuchElementException as e:
#     print(e)
#     driver.quit()

# print(1)

driver.quit()