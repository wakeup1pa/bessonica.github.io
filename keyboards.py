from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url="https://wakeup1pa.github.io/bessonica.github.io/")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Site', web_app=web_app)]
    ],
    resize_keyboard=True
)
