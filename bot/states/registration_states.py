from aiogram.fsm.state import State, StatesGroup

class RegistrationStates(StatesGroup):
    ism = State()
    familiya = State()
    photo = State()
    telefon = State()
    button = State()
    long = State()
    lat = State()