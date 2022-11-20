import telebot
from telebot import types
import scrape
import config
import messages
import db
import payment
import psycopg2
import schedule
from time import sleep
import asyncio


bot = telebot.TeleBot(token=config.TELEGRAM_API_TOKEN)
ref_url = "http://t.me/airogramhashim_bot?start={}"

@bot.message_handler(commands=['menu'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_scrape = types.KeyboardButton(text="📈eXpert")
    button_payment = types.KeyboardButton(text="💸Оплата")
    button_faq = types.KeyboardButton(text="📃FAQ")
    button_support = types.KeyboardButton(text="🛠Support")
    button_ref = types.KeyboardButton(text="⚜️Реферальная ссылка")
    markup.row(button_scrape, button_payment, button_faq, button_support, button_ref)
    if message.chat.id in config.ADMINS:
        button_admin = types.KeyboardButton(text="⚠Админ панель")
        markup.row(button_admin)
    bot.send_message(message.chat.id, "💡Меню", reply_markup=markup)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, text="📊Добро пожаловать в P2P-Россия")
    db.update_ref(bot=bot,id=message.chat.id,message=message)
    schedule.every().day.at('00:00').do(db.update_subscription, message.chat.id, bot)
    while True:
        schedule.run_pending()
        sleep(1)





@bot.message_handler(content_types=['text'])
def handle_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    connection = psycopg2.connect(
        host=config.PG_HOST,
        database=config.PG_DB,
        user=config.PG_USER,
        password=config.PG_PASSWORD)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("SELECT user_id VALUES FROM users")
    x = map(list, list(cursor.fetchall()))
    x = sum(x, [])
    cursor.execute(f"SELECT subscription VALUES FROM users WHERE user_id = {message.chat.id}")
    count = map(list, list(cursor.fetchall()))
    count = sum(count, [])
    if count[0] > 0 or message.chat.id in config.ADMINS:
        button_back = types.InlineKeyboardButton(text='⬅️Назад', callback_data="back")
        if message.text == '⬅️Назад':
            markup.row(button_back)
            start(message)
        if message.text == "📃FAQ":
            bot.send_message(message.chat.id, text=messages.faq_message,
                             reply_markup=markup, parse_mode="MarkdownV2")

        if message.text == "🛠Support":
            markup.row(button_back)
            bot.send_message(message.chat.id, text=messages.support_message, reply_markup=markup, parse_mode="MarkdownV2")
        if message.text == "⚜️Реферальная ссылка":
            markup.row(button_back)
            bot.send_message(message.chat.id,
                             text=f"⚜️Ваша реферальная ссылка: {ref_url.format(message.chat.id)}\n\nПоделитесь реферальной ссылкой для приглашения, чтобы получать дополнительные бонусы 🎁",
                             reply_markup=markup)
        if message.text == "💸Оплата":
            button_payment_method = types.KeyboardButton(text="Другой способ")
            markup.row(button_payment_method,button_back)
            payment.pay(message.chat.id,bot, markup)
            db.add_subscription(message.chat.id)
        if message.text == "Другой способ":
            bot.send_message(message.chat.id, text=messages.payment_message, reply_markup=markup, parse_mode="MarkdownV2")
        if message.text == "📈eXpert":
            button_normal_data = types.KeyboardButton(text='⛓Получить связки')
            button_exclusive_data = types.KeyboardButton(text='💎Получить эксклюзивные связки')
            markup.row(button_normal_data,button_exclusive_data,button_back)
            bot.send_message(message.chat.id, text='Выберите способ получения связок',reply_markup=markup)
        if message.text == "💎Получить эксклюзивные связки":
            bot.send_message(message.chat.id, text='Идет анализ таблицы связок.Пожалуйста подождите немного.')
            scrape.get_exclusive_data(message.chat.id,bot)
        if message.text == "⛓Получить связки":
            bot.send_message(message.chat.id, text='Идет анализ таблицы связок.Пожалуйста подождите немного.')
            scrape.get_normal_data(message.chat.id,bot)


        if message.chat.id in config.ADMINS and message.text == "⚠Админ панель":
            button_add = types.KeyboardButton(text="✅Добавить пользователя")
            button_delete = types.KeyboardButton(text="❌Удалить пользователя")
            button_spam = types.KeyboardButton(text="✉️Рассылка")
            button_show_subscribers = types.KeyboardButton(text="👤Список подписок")
            markup.add(button_add,button_delete,button_spam,button_show_subscribers, button_back)
            bot.send_message(message.chat.id, text='Панель управления администратора',reply_markup=markup)
        if message.text == "✅Добавить пользователя":
            msg = bot.send_message(message.chat.id, text="Введите ID пользователя")
            bot.register_next_step_handler(msg,db.add_user,bot)


        if message.text == "❌Удалить пользователя":
            msg = bot.send_message(message.chat.id, text="Введите ID пользователя")
            bot.register_next_step_handler(msg,db.delete_user,bot)
        if message.text == "✉️Рассылка":
            msg = bot.send_message(message.chat.id, text="Введите сообщение для рассылки")
            bot.register_next_step_handler(msg,db.mailing,bot)
        if message.text == "👤Список подписок":
            db.get_subscribers(message.chat.id, bot)
    else:
        button_faq = types.KeyboardButton(text="📃FAQ")
        markup.row(button_faq)
        bot.send_message(message.chat.id, text=messages.access_message, reply_markup=markup, parse_mode="MarkdownV2")
        bot.id
        if message.text == "📃FAQ":
            bot.send_message(message.chat.id, text=messages.faq_message,
                             reply_markup=markup, parse_mode="MarkdownV2")


bot.infinity_polling(none_stop=True)
