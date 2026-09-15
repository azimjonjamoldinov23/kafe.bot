from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()


menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍔 Menyu"),
            KeyboardButton(text="🛒 Buyurtma")
        ],
        [
            KeyboardButton(text="📋 Buyurtmalar"),
            KeyboardButton(text="ℹ️ Yordam")
            
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Bo'limni tanlang"
)


@router.message(CommandStart())
async def start(message: Message):

    start_matni = (
        "☕️ <b>Xush kelibsiz!</b>\n\n"
        "🍔 Mazali taomlar\n"
        "🥤 Sovuq ichimliklar\n"
        "🍰 Shirinliklar\n\n"
        "👇 Buyurtma berish uchun menyuni tanlang!"
    )

    await message.answer(
        start_matni,
        parse_mode="HTML",
        reply_markup=menyu
    )