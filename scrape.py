import gspread
from google.oauth2.service_account import Credentials

url = "https://docs.google.com/spreadsheets/d/1T7ja7C606oVXVG_FjWJWeB4vY_8Xe5IdgPDCxiuGIZM/edit#gid=0"
scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file("creds/client_secret.json", scopes=scope)

def process_data(bank,currency,bot,id):
    procents = []
    currency_list = ['USDT>BTC','USDT>ETH','USDT>BUSD','USDT>SHIB','USDT>BNB','USDT>RUB','BTC>USDT','BTC>ETH','BTC>BNB','BTC>BUSD','ETH>BTC','ETH>BNB','BUSD>BTC','BUSD>ETH','BUSD>BNB','BUSD>SHIB','BNB>ETH','RUB>BUSD','RUB>BNB']
    for k, z in enumerate(currency):
        z = z.replace(',','.')
        procents.append(float(z))
    value_currency = procents.index(max(procents))
    bot.send_message(id,text=f"✅{bank} ➡ {currency_list[value_currency]} ➡ {max(procents)}%")
    procents = []

def get_normal_data(id,bot):
    client = gspread.authorize(creds)
    google_sh = client.open("P2P_New")
    wsh = google_sh.worksheet('Binance_RUB')
    tinkoff_tinkoff = wsh.get_values('B61:W61')
    tinkoff_rosbank = wsh.get_values('B62:W62')
    tinkoff_qiwi = wsh.get_values('B63:W63')
    tinkoff_yandex = wsh.get_values('B64:W64')
    tinkoff_raifisen = wsh  .get_values('B65:W65')
    rossbank_tinkoff = wsh.get_values('B66:W66')
    rossbank_rossbank = wsh.get_values('B67:W67')
    rossbank_qiwi = wsh.get_values('B68:W68')
    rossbank_yandex = wsh.get_values('B69:W69')
    rossbank_raifisen = wsh.get_values('B70:W70')
    qiwi_tinkoff = wsh.get_values('B71:W71')
    qiwi_rosbank = wsh.get_values('B72:W72')
    qiwi_qiwi = wsh.get_values('B73:W73')
    qiwi_yandex = wsh.get_values('B74:W74')
    qiwi_raifisen = wsh.get_values('B75:W75')
    yandex_tinkoff = wsh.get_values('B76:W76')
    yandex_rosbank = wsh.get_values('B77:W77')
    yandex_qiwi = wsh.get_values('B78:W78')
    yandex_yandex = wsh.get_values('B79:W79')
    yandex_raifisen = wsh.get_values('B80:W80')
    raifisen_tinkoff = wsh.get_values('B81:W81')
    raifisen_rosbank = wsh.get_values('B82:W82')
    raifisen_qiwi = wsh.get_values('B83:W83')
    raifisen_yandex = wsh.get_values('B84:W84')
    raifisen_raifisen = wsh.get_values('B85:W85')


    tinkoff_tinkoff_ = map(list, list(tinkoff_tinkoff))
    tinkoff_tinkoff_ = sum(tinkoff_tinkoff_, [])
    proc_1 = []
    tinkoff_rosbank_ = map(list, list(tinkoff_rosbank))
    tinkoff_rosbank_ = sum(tinkoff_rosbank_, [])
    proc_2 = []
    tinkoff_qiwi_ = map(list, list(tinkoff_qiwi))
    tinkoff_qiwi_ = sum(tinkoff_qiwi_, [])
    tinkoff_yandex_ = map(list, list(tinkoff_yandex))
    tinkoff_yandex_ = sum(tinkoff_yandex_, [])
    tinkoff_raifisen_ = map(list, list(tinkoff_raifisen))
    tinkoff_raifisen_ = sum(tinkoff_raifisen_, [])
    rossbank_tinkoff_ = map(list, list(rossbank_tinkoff))
    rossbank_tinkoff_ = sum(rossbank_tinkoff_, [])
    rossbank_rossbank_ = map(list, list(rossbank_rossbank))
    rossbank_rossbank_ = sum(rossbank_rossbank_, [])
    rossbank_qiwi_ = map(list, list(rossbank_qiwi))
    rossbank_qiwi_ = sum(rossbank_qiwi_, [])
    rossbank_yandex_ = map(list, list(rossbank_yandex))
    rossbank_yandex_ = sum(rossbank_yandex_, [])
    rossbank_raifisen_ = map(list, list(rossbank_raifisen))
    rossbank_raifisen_ = sum(rossbank_raifisen_, [])
    qiwi_tinkoff_ = map(list, list(qiwi_tinkoff))
    qiwi_tinkoff_ = sum(qiwi_tinkoff_, [])
    qiwi_rosbank_ = map(list, list(qiwi_rosbank))
    qiwi_rosbank_ = sum(qiwi_rosbank_, [])
    qiwi_qiwi_ = map(list, list(qiwi_qiwi))
    qiwi_qiwi_ = sum(qiwi_qiwi_, [])
    qiwi_yandex_ = map(list, list(qiwi_yandex))
    qiwi_yandex_ = sum(qiwi_yandex_, [])
    qiwi_raifisen_ = map(list, list(qiwi_raifisen))
    qiwi_raifisen_ = sum(qiwi_raifisen_, [])
    yandex_tinkoff_ = map(list, list(yandex_tinkoff))
    yandex_tinkoff_ = sum(yandex_tinkoff_, [])
    yandex_rosbank_ = map(list, list(yandex_rosbank))
    yandex_rosbank_ = sum(yandex_rosbank_, [])
    yandex_qiwi_ = map(list, list(yandex_qiwi))
    yandex_qiwi_ = sum(yandex_qiwi_, [])
    yandex_yandex_ = map(list, list(yandex_yandex))
    yandex_yandex_ = sum(yandex_yandex_, [])
    yandex_raifisen_ = map(list, list(yandex_raifisen))
    yandex_raifisen_ = sum(yandex_raifisen_, [])
    raifisen_tinkoff_ = map(list, list(raifisen_tinkoff))
    raifisen_tinkoff_ = sum(raifisen_tinkoff_, [])
    raifisen_rosbank_ = map(list, list(raifisen_rosbank))
    raifisen_rosbank_ = sum(raifisen_rosbank_, [])
    raifisen_qiwi_ = map(list, list(raifisen_qiwi))
    raifisen_qiwi_ = sum(raifisen_qiwi_, [])
    raifisen_yandex_ = map(list, list(raifisen_yandex))
    raifisen_yandex_ = sum(raifisen_yandex_, [])
    raifisen_raifisen_ = map(list, list(raifisen_raifisen))
    raifisen_raifisen_ = sum(raifisen_raifisen_, [])
    all = tinkoff_tinkoff_,tinkoff_rosbank_,tinkoff_qiwi_,tinkoff_yandex_,tinkoff_raifisen_,rossbank_tinkoff_,rossbank_rossbank_,rossbank_qiwi_,rossbank_yandex_,rossbank_raifisen_,qiwi_tinkoff_,qiwi_rosbank_,qiwi_qiwi_,qiwi_yandex_,qiwi_raifisen_,yandex_tinkoff_,yandex_rosbank_,yandex_qiwi_,yandex_yandex_,yandex_raifisen_,raifisen_tinkoff_,raifisen_rosbank_,raifisen_qiwi_,raifisen_yandex_,raifisen_raifisen_
    banks = ['С TinkoffNew на TinkoffNew','С TinkoffNew на RosBankNew','С TinkoffNew на QIWI','С TinkoffNew на YandexMoneyNew','С TinkoffNew на RaiffeisenBank','С RosBankNew на TinkoffNew','С RosBankNew на RosBankNew','С RosBankNew на QIWI','С RosBankNew на YandexMoneyNew','С RosBankNew на RaiffeisenBank','С QIWI на TinkoffNew','С QIWI на RosBankNew','С QIWI на QIWI','С QIWI на YandexMoneyNew','С QIWI на RaiffeisenBank','С YandexMoneyNew на TinkoffNew','С YandexMoneyNew на RosBankNew','С YandexMoneyNew на QIWI','С YandexMoneyNew на YandexMoneyNew','С YandexMoneyNew на RaiffeisenBank','С RaiffeisenBank на TinkoffNew','С RaiffeisenBank на RosBankNew','С RaiffeisenBank на QIWI','С RaiffeisenBank на YandexMoneyNew','С RaiffeisenBank на RaiffeisenBank']
    for index,bank in enumerate(all):
        process_data(currency=bank,bank=banks[index],bot=bot,id=id)


def get_exclusive_data(id,bot):
    client = gspread.authorize(creds)
    google_sh = client.open("P2P_New")
    wsh = google_sh.worksheet('Binance_RUB')
    for count in range(4,9):
        bot.send_message(id,text=f"✅Процент: {wsh.acell(f'V{count}').value}%\n{wsh.acell(f'W{count}').value}")

