from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.handlers.user.message import ZodiacCompatibility
from src.keyboards.inline import zodiac_dict, get_fms_inline_zodiac_keyboard
from src.utils.httprequests import get_text_horoscope, get_text_compatibility

router = Router()


@router.callback_query(F.data.startswith("zdc_"))
async def zodiac_cb(cb: CallbackQuery):
    zodiac_sign = cb.data.split("_")[1]
    response = await get_text_horoscope(zodiac_sign)

    text = (
        f"Гороскоп на сегодня для ✨*{zodiac_dict[zodiac_sign][0]}*✨:\n\n"
        f"{response}"
    )

    await cb.message.delete()

    await cb.answer("")
    await cb.message.answer(text)


@router.callback_query(ZodiacCompatibility.first_sign)
async def first_z_msg(cb: CallbackQuery, state: FSMContext):
    await state.update_data(first_sign=cb.data)

    await cb.message.delete()

    await cb.answer("")
    await cb.message.answer(
        "2) Знак зодиака мужчины?", reply_markup=get_fms_inline_zodiac_keyboard()
    )
    await state.set_state(ZodiacCompatibility.second_sign)


@router.callback_query(ZodiacCompatibility.second_sign)
async def second_z_msg(cb: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    first_sign = user_data["first_sign"]
    second_sign = cb.data.lower()

    await state.clear()

    response = await get_text_compatibility(first_sign, second_sign)

    if type(response) == str:
        await cb.answer("")
        await cb.message.answer(response)
        return

    relationship_type, love_compatibility, description = await get_text_compatibility(
        first_sign, second_sign
    )

    text = (
        f"✨Гороскоп совместимости✨: *{''.join(zodiac_dict[first_sign])} + {''.join(zodiac_dict[second_sign])}*\n\n"
        f"Тип отношений: *{relationship_type}*\n\n"
        f"*{love_compatibility}*\n\n{description}"
    )

    await cb.message.delete()

    await cb.answer("")
    await cb.message.answer(text)