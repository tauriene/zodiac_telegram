from aiogram.utils.keyboard import InlineKeyboardBuilder

zodiac_dict = {
    "aries": ["Овен", "♈️"],
    "taurus": ["Телец", "♉️"],
    "gemini": ["Близнецы", "♊️"],
    "cancer": ["Рак", "♋️"],
    "leo": ["Лев", "♌️"],
    "virgo": ["Дева", "♍️"],
    "libra": ["Весы", "♎️"],
    "scorpio": ["Скорпион", "♏️"],
    "sagittarius": ["Стрелец", "♐️"],
    "capricorn": ["Козерог", "♑️"],
    "aquarius": ["Водолей", "♒️"],
    "pisces": ["Рыбы", "♓️"],
}


def get_inline_zodiac_keyboard():
    builder = InlineKeyboardBuilder()

    for key in zodiac_dict:
        builder.button(
            text=f"{zodiac_dict[key][0]}{zodiac_dict[key][1]}",
            callback_data=f"zdc_{key}",
        )

    builder.adjust(3)
    return builder.as_markup()

def get_fms_inline_zodiac_keyboard():
    builder = InlineKeyboardBuilder()

    for key in zodiac_dict:
        builder.button(
            text=f"{zodiac_dict[key][0]}{zodiac_dict[key][1]}",
            callback_data=f"{key}",
        )

    builder.adjust(3)
    return builder.as_markup()
