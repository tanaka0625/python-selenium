from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import scroll
import gspread
import datetime
import make_credentials

import info

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://selenium:4444/wd/hub',
             options = options
             )

url = 'https://www.instagram.com/accounts/login/' # テストでアクセスするURLを指定
driver.get(url)

driver.implicitly_wait(10)

try:

    # ログイン
    username_box = driver.find_element(By.XPATH, "//input[@name='username']")
    password_box = driver.find_element(By.XPATH, "//input[@name='password']")
    btn = driver.find_element(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']")
    username = info.returnu()
    password = info.returnp()
    username_box.send_keys(username)
    password_box.send_keys(password)
    btn.click()
    time.sleep(10)

 
    btns = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]')
    print(len(btns))
    btns[5].click()
   

    time.sleep(15)
    driver.quit()

except Exception as e:
    print("miss")
    print("")
    print(e)
    time.sleep(5)


    driver.quit()