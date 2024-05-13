from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import scroll
import gspread
import datetime

import make_credentials


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
        if(i==0):
            item = ["タイトル", "リンク"]
        elif(i>0):
            title = titles[i].text
            link = titles[i].parent["href"]
            item = [title, link]

        items.append(item)


    time.sleep(5)


    # 検索結果をデータフレームに成型
    df = pd.DataFrame(items)
    print(df)

    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    key_pass = "./key.json"

    # credentials作成
    credentials = make_credentials.do(scopes, key_pass)

    # Auth2のクレデンシャルを使用してGoogleAPIにログイン
    gc = gspread.authorize(credentials)

    # スプレッドシートの新規作成
    dt_now = datetime.datetime.now().strftime("%Y/%m/%d/ %H:%M:%S")
    name = dt_now
    ss = gc.create(name, "1dATyJ6wK3jpw3_otIGVY6VnNpoiGWc0h")

    # シートを特定する（シートインデックスで特定）
    st = ss.get_worksheet(0) #0は左から1番目のシート

    # シート名変更
    st_name = "記事一覧"
    st.update_title(st_name)

    # 書き込み
    st.append_rows(values=items, table_range='B2')

    driver.quit()

except Exception as e:
    print("miss")
    print("")
    print(e)
    time.sleep(5)


    driver.quit()