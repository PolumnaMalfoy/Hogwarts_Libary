from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

product = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Collectible Figures"),
            KeyboardButton(text="Posters"),
            KeyboardButton(text="Cosplay"),
        ],
        [
            KeyboardButton(text="Mangas"),
            KeyboardButton(text="Stickers"),
            KeyboardButton(text="Anime Stationary"),
        ]

    ]



)