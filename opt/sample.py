from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://selenium:4444/wd/hub',
             options = options
             )

# print(driver)

driver.implicitly_wait(1)

url = 'https://datascience-beginer.com/' # テストでアクセスするURLを指定
driver.get(url)

time.sleep(1)
driver.save_screenshot('test.png') # アクセスした先でスクリーンショットを取得
driver.quit()

