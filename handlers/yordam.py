from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("yordam"))
async def yordam_handler(message: Message):
    yordam_matni = (
        "ℹ️ <b>Botdan foydalanish bo'yicha qo'llanma</b>\n\n"
        "☕️ <b>Assalomu alaykum!</b>\n"
        "Kafe botimiz orqali menyu bilan tanishishingiz va "
        "o'zingizga yoqqan taomlarni tanlashingiz mumkin.\n\n"

        "📋 <b>Menyu</b>\n"
        "Kafemizdagi barcha taom va ichimliklar ro'yxatini ko'rishingiz mumkin.\n\n"

        "🍔 <b>Taomlar</b>\n"
        "Mazali va yangi tayyorlangan taomlarimizdan "
        "o'zingizga yoqqanini tanlang.\n\n"

        "🥤 <b>Ichimliklar</b>\n"
        "Issiq va sovuq ichimliklarimiz bilan tanishing.\n\n"

        "🛒 <b>Buyurtma</b>\n"
        "Kerakli mahsulotlarni tanlab, buyurtmangizni shakllantiring.\n\n"

        "🔄 <b>/start</b> — Botni qayta ishga tushirish.\n"
        "ℹ️ <b>/yordam</b> — Ushbu qo'llanmani ko'rsatish.\n\n"

        "✨ <b>Yoqimli ishtaha!</b>\n"
        "Bizni tanlaganingiz uchun rahmat! ❤️"
    )

    await message.answer(yordam_matni, parse_mode="HTML")