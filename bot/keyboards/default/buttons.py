from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


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