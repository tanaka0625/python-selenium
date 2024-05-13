# 一番下までスクロールする

import time

def do(driver, last_top: int=1):
    win_height = driver.execute_script("return window.innerHeight")

    while True:

        last_height = driver.execute_script("return document.body.scrollHeight")
        
        
        top = last_top - 1

        
        while top < last_height:
            top += int(win_height * 0.8)
            driver.execute_script("window.scrollTo(0, %d)" % top)
            time.sleep(0.5)

        
        time.sleep(1)
        new_last_height = driver.execute_script("return document.body.scrollHeight")

        
        if last_height == new_last_height:
            break

        #次のループのスクロール位置を設定
        last_top = last_height