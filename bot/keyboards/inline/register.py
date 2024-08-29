from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def registrationButton(button: str):
    registrationButton = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Ro'yxatdan o'tish",
                                     callback_data=f"registration:{button}"),
            ]
        ]


    )
    return registrationButton