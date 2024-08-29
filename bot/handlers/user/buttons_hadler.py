from aiogram.types import Message
from bot.keyboards.default.Products import product
from bot.keyboards.default.office import office
from bot.keyboards.default.about_us import us

from loader import dp

@dp.message(lambda message: message.text == "Products")
async def product_handler(message: Message):
    await message.answer("In our Anime store there're: ",
                         reply_markup=product)

@dp.message(lambda message: message.text == "Private office")
async def product_handler(message: Message):
    await message.answer("You can contact with us: ",
                         reply_markup=office)
@dp.message(lambda message: message.text == "About us")
async def product_handler(message: Message):
    await message.answer("About us: ",
                         reply_markup=us)
