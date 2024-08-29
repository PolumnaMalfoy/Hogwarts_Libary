from aiogram.types import Message
from bot.keyboards.default.buttons import menu_Buttnos
from bot.keyboards.inline.register import registrationButton
from loader import dp

@dp.message(lambda message: message.text == "Collectible Figures")
async def figures(message: Message):
    response = """In our store there are lots of anime figures from different anime,for example: Attack on Titan
,Death Note,Naruto, Jut Jutsen Kaisen and other"""
    await message.answer(response, reply_markup=registrationButton("Collectible Figures"))

@dp.message(lambda message: message.text == "Posters")
async def posters(message: Message):
    response = """In our store there are lots of anime posters in good condition and in different size i.e. A3,A4  from different anime,for example: Attack on Titan
,Death Note,Naruto, Jut Jutsen Kaisen and other"""
    await message.answer(response, reply_markup=registrationButton("Posters"))

@dp.message(lambda message: message.text == "Cosplay")
async def cosplay(message: Message):
    response = """In our store there are lots of anime cosplay from different anime,for example:
Attack on Titan
,Death Note,Naruto, Jut Jutsen Kaisen and other. It's suitable for women and men"""
    await message.answer(response, reply_markup=registrationButton("Cosplay"))

@dp.message(lambda message: message.text == "Mangas")
async def manga(message: Message):
    response = """In our store there are lots of manga  wich adopted to different anime,for example:
Attack on Titan
,Death Note,Naruto, Jut Jutsen Kaisen and other. There are 150.000 manga """
    await message.answer(response, reply_markup=registrationButton("Mangas"))

@dp.message(lambda message: message.text == "Stickers")
async def sticker(message: Message):
    response = """
    """
    await message.answer(response, reply_markup=registrationButton("Stickers"))

@dp.message(lambda message: message.text == "Anime Stationary")
async def anime(message: Message):
    response = """In our store there are lots of anime stationary like anime pens,pencils,
     notebooks and also bags with anime print, from different anime,for example: Attack on Titan
,Death Note,Naruto, Jut Jutsen Kaisen and other"""
    await message.answer(response, reply_markup=registrationButton("Anime Stationary"))