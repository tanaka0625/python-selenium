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
    scroll.do(driver)

    time.sleep(10)

    # ページのソースコードを取得
    html = driver.page_source.encode('utf-8')

    # タイトルを収集 
    soup = BeautifulSoup(html, 'html.parser')
    selector1 = ".LC20lb"
    titles = soup.select(selector1)
    # print(len(titles))

    # for title in titles:
    #     print(title.text)
    #     print('')

    # driver.quit()

    #タイトルのリンクを収集
    # selector2 = ".yuRUbf > div > span > a"
    # links = soup.select(selector2)
    # # print(links[0]['href'])


    # print(len(links))

    # for link in links:
    #     print(link["href"])
    #     print('')


    # 出力用の配列を作成
    items = []
    for i in range(len(titles)):
        title = titles[i].text
        # link = links[i]["href"]
        link = titles[i].parent["href"]
        item = [title, link]

        items.append(item)

        print(items[i])
        print("")
        print(i)
    
    # print(len(items))

    


    # time.sleep(30)




    driver.quit()

except Exception as e:
    print("miss")
    print("")
    print(e)
    time.sleep(5)


    driver.quit()