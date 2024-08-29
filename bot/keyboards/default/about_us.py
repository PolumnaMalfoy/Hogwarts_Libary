from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

us = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Our history"),
        KeyboardButton(text="Our achievements"),]
    ]
)