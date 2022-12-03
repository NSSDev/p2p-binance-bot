from SimpleQIWI import *
import config
import time

token = config.QIWI_TOKEN
phone = config.QIWI_PHONE

def pay(id, bot, markup):
    counter = 0
    start_time = time.time()
    api = QApi(token=token, phone=phone)
    price = 10
    comment = api.bill(
        price, comment=id)
    bot.send_message(id,
                     text=f"💰ВЫСТАВЛЕНИЕ СЧЕТА💰\n\n💳Переведите {price} рублей\n📲На счет QIWI: {phone}\n✉С комментарием: '{id}' без кавычек ",
                     reply_markup=markup)
    bot.send_message(id,text="СЧЕТ ДЕЙСТВИТЕЛЕН НА 3 МИНУТЫ")
    api.start()
    while int(time.time()-start_time) != 180:
        if api.check(comment):
            counter += 1
            bot.send_message(id,
                             text=f"⚜ Благодарим за покупку ! Вы купили подписку/У вас уже имеется подписка на 1 месяц. ⚜",
                             reply_markup=markup)
            break
        time.sleep(1)
    api.stop()
