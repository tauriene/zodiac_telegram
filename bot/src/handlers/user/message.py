from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from src.keyboards.inline import (
    get_inline_zodiac_keyboard,
    get_fms_inline_zodiac_keyboard,
)

router = Router()


class ZodiacCompatibility(StatesGroup):
    first_sign = State()
    second_sign = State()


@router.message(CommandStart())
async def start_msg(msg: Message):
    await msg.answer(
        "Добро пожаловать! Хочешь узнать, какие сюрпризы подкинет тебе судьба? "
        "Я здесь, чтобы рассказать о твоем гороскопе!\n\n"
        "*Попробуй мои команды*:\n"
        "/horoscope - узнать свой гороскоп\n"
        "/compatibility - проверить совместимость знаков зодиака"
    )


@router.message(Command("horoscope"))
async def horoscope_msg(msg: Message):
    await msg.answer(
        "Выбери знак зодиака:", reply_markup=get_inline_zodiac_keyboard()
    )


@router.message(StateFilter(None), Command("compatibility"))
async def compatibility_msg(msg: Message, state: FSMContext):

    await msg.answer(
        "1) Знак зодиака женщины?", reply_markup=get_fms_inline_zodiac_keyboard()
    )
    await state.set_state(ZodiacCompatibility.first_sign)
