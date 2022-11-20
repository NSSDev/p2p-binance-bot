import gspread
from google.oauth2.service_account import Credentials

url = "google sheet url"
scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("creds/client_secret.json", scopes=scope)


def get_exclusive_data(id,bot):
    client = gspread.authorize(creds)
    google_sh = client.open("P2P")
    wsh = google_sh.worksheet('P2P')
    for count in range(4,14):
        bot.send_message(id,text=f"✅{wsh.acell(f'T{count}').value}")

def get_normal_data(id,bot):
    currency = ['BTC/USDT','BTC/RUB','BTC/BUSD','ETH/USDT','ETH/RUB','ETH/BUSD','SHIB/USDT']
    client = gspread.authorize(creds)
    sh = client.open_by_key("1oks3xOVquxdE78vs0M2pVF5S3xzKL4fZgWKmDpnLk-U")
    taker_maker = "💸Покупаю как тейкер, продаю как мейкер💸"
    qy = sh.values_get("A45:H45")['values']
    qr = sh.values_get("A47:H47")['values']
    yr = sh.values_get("A54:H54")['values']
    rq = sh.values_get("A65:H65")['values']
    ry = sh.values_get("A66:H66")['values']
    bot.send_message(id, text=f"{taker_maker}\n\n\t\t\t\t\t\t\t{currency[0]} || {currency[1]} || {currency[2]} || {currency[3]} || {currency[4]} || {currency[5]} || {currency[6]}\n👉{qy}\n👉{qr}\n👉{yr}\n👉{rq}\n👉{ry}")




