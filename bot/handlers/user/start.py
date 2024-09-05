from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram import html
from keyboards.default.buttons import menu_Buttnos
from keyboards.inline.register import registrationButton

from loader import dp

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hi!, {html.bold(message.from_user.full_name)}!, This is 'Shiganshina' anime"
                         f" store! You're welcome!", reply_markup=menu_Buttnos)


    # await message.answer(f"Assolomu alaykum,{html.bold(message.from_user.full_name)}!"
    #                      f"\nO'quv markazimizga xush kelibsiz!"
    #                      f"\nSizga qanday yordam bera olaman?"
    #                      f"\n Kerakli bo'limni tanlang! ", reply_markup=menu_Buttnos)
