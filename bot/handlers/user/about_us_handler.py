from aiogram.types import Message
from bot.keyboards.default.buttons import menu_Buttnos
from bot.keyboards.inline.register import registrationButton
from loader import dp

@dp.message(lambda message: message.text == "Our history")
async def figures(message: Message):
    response = """ Our founder of the store is Levi Ackerman, who opened it in 2019, when the coronavirus had just begun to spread,
and then he decided to please the guys of anime and manga series with his own store, 
because these products could please an anime fan who had fallen ill with corona,
 and this store still pleases anime fans and manga fans"""
    await message.answer(response, reply_markup=registrationButton("Our history"))


@dp.message(lambda message: message.text == "Our achievements")
async def figures(message: Message):
    response = """ Our achieved goals and rewards
Now in 2024 our store can send its goods to 15 staranha, this is one of the biggest achievements for us,
and also in 2020 we received an award for being able to please more than 150,000 anime fans with our products"""
    await message.answer(response, reply_markup=registrationButton("Our achievements"))