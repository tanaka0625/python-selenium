# スプレッドシート作成

import gspread

from . import make_credentials

def do(name: str, folder_id: str):

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
    sh = gc.create(name, folder_id)

    return sh
