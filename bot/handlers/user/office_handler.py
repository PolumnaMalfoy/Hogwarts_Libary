from aiogram.types import Message
from bot.keyboards.default.buttons import menu_Buttnos
from bot.keyboards.inline.register import registrationButton
from loader import dp

@dp.message(lambda message: message.text == "Telegram")
async def telegram(message: Message):
    response = """ We have our telegram account you can write to us with this @polumn_malfoy
     And also call to us +998916551061
     our Administrator is Micassa Ackerman
     https://t.me/polumna_malfoy
      """
    await message.answer(response, reply_markup=registrationButton("Telegram"))

@dp.message(lambda message: message.text == "Instagram")
async def insta(message: Message):
    response = """We also have instagram account where you can watch posts with our products and achievements 
it's Slytherin_princcess 
our Administrator is Micassa Ackerman
https://t.me/polumna_malfoy"""
    await message.answer(response, reply_markup=registrationButton("Instagram"))

@dp.message(lambda message: message.text == "Tik-tok")
async def tt(message: Message):
    response = """ We also have our Tik-tok account @jjkdr
our Administrator is Micassa Ackerman
https://t.me/polumna_malfoy"""
    await message.answer(response, reply_markup=registrationButton("Tik-tok"))