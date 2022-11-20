import psycopg2
import config
import messages

subscription = 30


def connect():
    try:
        conn = psycopg2.connect(
            host=config.PG_HOST,
            database=config.PG_DB,
            user=config.PG_USER,
            password=config.PG_PASSWORD)
        conn.autocommit = True
        create_table(connection=conn)
    except Exception as e:
        print(f"[ERROR INFO]:\n{e}")


def add_subscription(id):
    conn = psycopg2.connect(
        host=config.PG_HOST,
        database=config.PG_DB,
        user=config.PG_USER,
        password=config.PG_PASSWORD)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"SELECT subscription VALUES FROM users WHERE user_id = {id}")
    # count = map(list, list(cursor.fetchall()))
    # count = sum(count, [])
    # if count[0] != 0:
    #     cursor.close()
    #     conn.close()
    # else:
    cursor.execute(f"UPDATE users SET subscription = 30 WHERE user_id = {id}")
    cursor.close()
    conn.close()


def update_subscription(id):
    conn = psycopg2.connect(
        host=config.PG_HOST,
        database=config.PG_DB,
        user=config.PG_USER,
        password=config.PG_PASSWORD)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"SELECT subscription VALUES FROM users WHERE user_id = {id}")
    x = map(list, list(cursor.fetchall()))
    x = sum(x, [])
    if x[0] == 0:
        cursor.close()
        conn.close()
    sql = f"""UPDATE users
    SET subscription = {x[0] - 1}
    WHERE user_id = {id};"""
    cursor.execute(sql)
    conn.close()


def get_subscribers(id, bot):
    conn = psycopg2.connect(
        host=config.PG_HOST,
        database=config.PG_DB,
        user=config.PG_USER,
        password=config.PG_PASSWORD)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"""SELECT username VALUES FROM users WHERE subscription > 0""")
    all_subs = map(list, list(cursor.fetchall()))
    all_subs = sum(all_subs, [])
    bot.send_message(id, text=f"Список подписок:")
    for sub in all_subs:
        bot.send_message(id, text=f"@{sub}")


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT NOT NULL,
    username CHAR(25) NOT NULL,
    subscription INT NOT NULL,
    who_invited BIGINT,
    subscription_date TIMESTAMP NOT NULL DEFAULT NOW());""")
    connection.close()
    cursor.close()


def add_user(message, bot):
    try:
        conn = psycopg2.connect(
            host=config.PG_HOST,
            database=config.PG_DB,
            user=config.PG_USER,
            password=config.PG_PASSWORD)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users ( user_id, username, subscription, who_invited ) VALUES (%s, %s, %s, %s)',(message.text, message.from_user.username, 30, 1))
        bot.send_message(message.chat.id, text=f'Пользователь {message.text} добавлен')
        print(f'Администратор добавил пользователя {message.text} в БД')
        cursor.close()
        conn.close()

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, text="Неправильный формат.")


def delete_user(message, bot):
    try:
        sql = f"""DELETE FROM users WHERE user_id =  ({message.text});"""
        conn = psycopg2.connect(
            host=config.PG_HOST,
            database=config.PG_DB,
            user=config.PG_USER,
            password=config.PG_PASSWORD)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(sql)
        bot.send_message(message.chat.id, text=f'Пользователь {message.text} удален из базы данных')
        print(f'Администратор удалил пользователя {message.text} из БД')
        cursor.close()
        conn.close()
    except Exception:
        bot.send_message(message.chat.id, text="Неправильный формат.")


def update_ref(bot, id, message):
    connect()
    ref_id = message.text[-10:]
    conn = psycopg2.connect(
        host=config.PG_HOST,
        database=config.PG_DB,
        user=config.PG_USER,
        password=config.PG_PASSWORD)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""SELECT user_id VALUES FROM users""")
    all_users = map(list, list(cursor.fetchall()))
    all_users = sum(all_users, [])
    if id in all_users:
        bot.send_message(id, text="Вы уже зарегистрированы.")
    else:
        try:
            ref_id = int(ref_id)
            cursor.execute('INSERT INTO users ( user_id, username, subscription, who_invited ) VALUES (%s, %s, %s, %s)',
                           (id, message.from_user.username, 0, ref_id))
        except:
            cursor.execute('INSERT INTO users ( user_id, username, subscription, who_invited ) VALUES (%s, %s, %s, %s)',
                           (id, message.from_user.username, 0, 0))
        cursor.execute(f"SELECT subscription VALUES FROM users WHERE user_id = {id}")
        my_subs = map(list, list(cursor.fetchall()))
        my_subs = sum(my_subs, [])
        ################################## доработать
        if my_subs[0] == 0 and id not in config.ADMINS:
            try:
                bot.send_message(id, text=messages.access_message, parse_mode="MarkdownV2")
                bot.id
            except Exception:
                pass
        cursor.execute(f"SELECT subscription VALUES FROM users WHERE user_id = {ref_id}")
        subs = map(list, list(cursor.fetchall()))
        subs = sum(subs, [])
        ref_id = int(ref_id)
        if ref_id == id:
            return
        if subs[0] == 0:
            cursor.close()
            conn.close()
            return
        else:
            sql = f"""UPDATE users
            SET subscription = {subs[0] + 10}
            WHERE user_id = {ref_id};"""
            print('Добавил баллы за рефералку')
            cursor.execute(sql)
            cursor.close()
            conn.close()


def mailing(message, bot):
    connection = psycopg2.connect(
        host=config.PG_HOST,
        database=config.PG_DB,
        user=config.PG_USER,
        password=config.PG_PASSWORD)
    cursor = connection.cursor()
    cursor.execute("SELECT user_id VALUES FROM users")
    all_users = map(list, list(cursor.fetchall()))
    all_users = sum(all_users, [])
    for user in all_users:
        bot.send_message(user, text=message.text)
