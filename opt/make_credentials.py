# googleAPI使用のためのcredentials作成

from oauth2client.service_account import ServiceAccountCredentials

#scopesの例
# scopes = [
#     'https://www.googleapis.com/auth/spreadsheets',
#     'https://www.googleapis.com/auth/drive'
# ] 

# key_passの例 "../key.json"
def do(scopes: list, key_pass: str):

    # Credentials 情報を取得
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        key_pass,
        scopes
    )

    return credentials