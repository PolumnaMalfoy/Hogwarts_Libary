from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location_reques = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Location", request_location=True),
        ]
    ]
)