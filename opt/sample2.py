from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup
import time

import scroll


options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://selenium:4444/wd/hub',
             options = options
             )

url = 'https://www.google.co.jp/' # テストでアクセスするURLを指定
# url = 'https://www.yahoo.co.jp/'
driver.get(url)

driver.implicitly_wait(10)

try:

    # 検索ボックスにpythonを入力
    search_bar = driver.find_element(By.ID, "APjFqb") #google
    # search_bar = driver.find_element(By.CSS_SELECTOR, "._1wsoZ5fswvzAoNYvIJgrU4") #yahoo
    search_bar.send_keys("python")

    # 検索
    search_bar.submit()

    time.sleep(5) #ページの更新が終わるのを待つ

    #無限スクロール
    scroll.do(driver,1)

    time.sleep(5) #ページの更新が終わるのを待つ

    # もっと見るボタンを取得
    next_btn = driver.find_element(By.XPATH, "//h3/div/span[@class='RVQdVd']")

    # もっと見るボタンを押下
    next_btn.click()

    time.sleep(5)

    #無限スクロール
    now_height = driver.execute_script("return document.body.scrollHeight")
    print(now_height)
    scroll.do(driver,now_height)

    time.sleep(5)



    # ページのソースコードを取得
    html = driver.page_source.encode('utf-8')

    # タイトルを収集 
    soup = BeautifulSoup(html, 'html.parser')
    selector1 = ".LC20lb"
    titles = soup.select(selector1)


    # 出力用の配列を作成
    items = []
    for i in range(len(titles)):
        title = titles[i].text
        link = titles[i].parent["href"]
        item = [title, link]

        items.append(item)

    time.sleep(5)

    driver.quit()

except Exception as e:
    print("miss")
    print("")
    print(e)
    time.sleep(5)


    driver.quit()