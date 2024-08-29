from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from bot.keyboards.inline.register import registrationButton
from aiogram.types import Message

menu_Buttnos = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text = "Products"),
            KeyboardButton(text = "Private office"),
            KeyboardButton(text = "About us")
        ]
    ]
)