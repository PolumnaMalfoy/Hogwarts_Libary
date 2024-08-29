from aiogram import F
from aiogram.types import CallbackQuery,Message
from aiogram.fsm.context import FSMContext
from bot.states.registration_states import RegistrationStates
from bot.keyboards.default.num import number_request
from bot.keyboards.default.loc import location_reques
from bot.data.register import registration
from bot.data.config import ADMINS

from loader import dp,bot

@dp.callback_query(lambda query: query.data.startswith('registration'))
async def registration_handler(query: CallbackQuery, state: FSMContext):
    course = query.data.split(":")[1]
    await state.set_state(RegistrationStates.ism)
    await state.update_data(button=course)
    await query.answer(cache_time=10)
    await query.message.answer("Enter your name to register: ")
@dp.message(RegistrationStates.ism)
async def ism_handler(message: Message, state: FSMContext):
    ism = message.text
    await state.update_data(ism=ism)
    await state.set_state(RegistrationStates.familiya)
    await message.answer("Enter your surname:")

@dp.message(RegistrationStates.familiya)
async def familiya_handler(message: Message, state:FSMContext):
    familiya = message.text
    await state.update_data(familiya=familiya)
    await state.set_state(RegistrationStates.telefon)
    await message.answer("To contact you"
                         "Enter your phone number:", reply_markup=number_request)

@dp.message(RegistrationStates.telefon)
async def telefon_handler(message: Message, state:FSMContext):
    if message.contact:
        telefon = message.contact.phone_number
    else:
        telefon = message.text
    await state.update_data(telefon=telefon)
    await state.set_state(RegistrationStates.photo)
    await message.answer("Rasmingizni yuboring:")

# @dp.message(RegistrationStates.telefon, F.contact)
# async def contact_hadler(message: Message, state: FSMContext):
#     telefon = message.contact.phone_number
#     await state.update_data(telefon=telefon)
#     await state.set_state(RegistrationStates.photo)
#     await message.answer("Rasmingizni yuboring:")

# data = await state.get_data()
    # await state.clear()
    # response = (f"Yangi ro'yxatdan o'tgan o'quvchi."
    #             f"\nFamiliya: {data['familiya']}"
    #             f"\n Ism: {data['ism']}"
    #             f"\nTelefon: {data['telefon']}"
    #             f"\nKurs: {data['kurs']}")
    # await bot.send_message(ADMINS[0],response)
    # await message.answer("Muvaffaqitatli ro'yxatdan o'tdingiz!")
@dp.message(RegistrationStates.photo)
async def phto_hadler(message: Message, state: FSMContext):
    if message.photo:
        file_id = message.photo[-1].file_id
        await state.update_data(photo=file_id)
        await state.set_state(RegistrationStates.long)
        await message.answer("Joyloshuvingizni yuboring:",
                             reply_markup=location_reques)
    else:
        await message.answer("No'tog'ri format, qaytadan rasm yuboring?")
        await state.set_state(RegistrationStates.photo)
@dp.message(RegistrationStates.long)
async def long_handler(message: Message, state: FSMContext):
    if message.location:
        long = message.location.longitude
        lat = message.location.latitude
        await state.update_data(long=long, lat=lat)
        data = await state.get_data()
        registration(data['ism'],
                     data['familiya'],
                     data['telefon'],
                     data['photo'],
                     data['kurs'],
                     data['long'],
                     data['lat']
                     )
    else:
        await message.answer("Noto'g'ri format, qaytdan yuboring?")
        await state.set_state(RegistrationStates.long)
