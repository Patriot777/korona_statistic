import logging
import mysql.connector
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1039158164:AAEjAAsit9-fiGFxydbj4IezhadCrVSKp_A'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Бота запущено, додайте його до своєї групи в телеграмі...")

@dp.message_handler()
async def echo(message: types.Message):
    # підключення до бази данних
    dataBase = mysql.connector.connect(
    host = 'cv400076.mysql.tools',
    user = 'cv400076_python',
    password = 'dt#59y+YT6',
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
   
    #await message.answer(b)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)