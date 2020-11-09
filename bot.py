import logging
import mysql.connector
import requests
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

import test_parser_korona

API_TOKEN = '1403327834:AAHqeAzU1pDRw_euv-o7KhLG_CPKlMbGl_U'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# def pars():
#     site_link = "https://index.minfin.com.ua/ua/reference/coronavirus/ukraine/"
#     request_link = requests.get(site_link)
#     soup = BeautifulSoup(request_link.text, 'html.parser')
#     korona = soup.find('strong', class_='black').text
    
#     return korona

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привіт, напишіть область для перевірки статистики.")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    # підключення до бази данних
    dataBase = mysql.connector.connect(
    host = 'cv400076.mysql.tools',
    user = 'cv400076_python',
    password = 'hSM4pbs9FK87',
    database = 'cv400076_python'
    )
    #Збір данних про користувача
    userID = message.from_user.id            # айді 
    userName = message.from_user.first_name  # імя
    text_user = message.text                 # текст повідомлення
    full_name = message.from_user.full_name  # Імя та прізвище
    is_bot = message.from_user.is_bot        # перевірка на бота
    last_name = message.from_user.last_name  # Прізвище
    local = message.from_user.locale         # Локалізація
    user_name = message.from_user.username   # Нік 
    url = message.from_user.url              # url          

    # запис в базу данних
    mycursor = dataBase.cursor()
    sql = "INSERT INTO users_telegram (user_id, user_name, text_user, url, local, last_name, is_bot, full_name, first_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (userID, user_name, text_user, url, str(local), last_name, is_bot, full_name, userName)
    mycursor.execute(sql, val)

    dataBase.commit()

    # Відповідь користувачу
    a = message.text
    c = str(a)
    b = test_parser_korona.starter(test_parser_korona.number_of_city(c))
    await message.answer(b)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
