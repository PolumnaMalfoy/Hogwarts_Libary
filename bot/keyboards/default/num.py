from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

number_request = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Phone number", request_contact=True)
        ]
    ]
)