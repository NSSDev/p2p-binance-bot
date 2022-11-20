from SimpleQIWI import *
import config
import time

token = config.QIWI_TOKEN
phone = config.QIWI_PHONE

def pay(id, bot, markup):
    start_time = time.time()
    api = QApi(token=token, phone=phone)
    price = 6000
    comment = api.bill(
        price, comment=id)
    bot.send_message(id,
                     text=f"💰ВЫСТАВЛЕНИЕ СЧЕТА💰\n\n💳Переведите {price} рублей\n📲На счет QIWI: {phone}\n✉С комментарием: '{id}' без кавычек ",
                     reply_markup=markup)
    bot.send_message(id,text="СЧЕТ ДЕЙСТВИТЕЛЕН НА 2 МИНУТЫ")
    api.start()
    while int(time.time()-start_time) != 120:
        if api.check(comment):
            bot.send_message(id,
                             text=f"⚜ Благодарим за покупку ! Вы получили подписку на 1 месяц. ⚜",
                             reply_markup=markup)
            break
        time.sleep(1)
    api.stop()
