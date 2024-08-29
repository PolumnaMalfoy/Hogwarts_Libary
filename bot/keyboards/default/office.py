from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

office = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Telegram"),
            KeyboardButton(text="Instagram"),
            KeyboardButton(text="Tik-tok")
        ]
    ]
)