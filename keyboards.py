from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

web_app_url = "https://wakeup1pa.github.io/bessonica.github.io/"

keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Site', url=web_app_url))
