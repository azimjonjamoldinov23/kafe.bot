from aiogram import F, Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

router = Router()


# =========================
# MAHSULOTLAR
# =========================

fast_food = {
    "🍕 Pizza": 35000,
    "🍔 Burger": 25000,
    "🍟 Kartoshka fri": 15000,
    "🌭 Hot-dog": 20000,
}

ichimliklar = {
    "🥤 Coca-Cola": 10000,
    "🧃 Sharbat": 12000,
    "☕️ Choy": 5000,
}

shirinliklar = {
    "🍰 Tort": 15000,
    "🍩 Donut": 10000,
}


# =========================
# BUYURTMALAR
# =========================

buyurtmalar = {}


# =========================
# 🍔 MENYU
# =========================


@router.message(F.text == "🍔 Menyu")
async def menyu_handler(message: Message):
    menyu_matni = (
        "📜 <b>KAFE MENYUSI</b>\n\n"
        "🍕 <b>Fast food:</b>\n"
        "• Pizza — 35 000 so'm\n"
        "• Burger — 25 000 so'm\n"
        "• Kartoshka fri — 15 000 so'm\n"
        "• Hot-dog — 20 000 so'm\n\n"
        "🥤 <b>Ichimliklar:</b>\n"
        "• Coca-Cola — 10 000 so'm\n"
        "• Sharbat — 12 000 so'm\n"
        "• Choy — 5 000 so'm\n\n"
        "🍰 <b>Shirinliklar:</b>\n"
        "• Tort — 15 000 so'm\n"
        "• Donut — 10 000 so'm"
    )

    await message.answer(menyu_matni, parse_mode="HTML")

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🥤 Ichimliklar", callback_data="category_drink"
                ),
                InlineKeyboardButton(
                    text="🍰 Shirinliklar", callback_data="category_sweet"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍕 Fast Food", callback_data="category_fast"
                )
            ],
        ]
    )

    await message.answer(
        "👇 <b>Nima buyurtma berasiz?</b>\n\nBo'limni tanlang:",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


# =========================
# 🍔 FAST FOOD
# =========================


@router.callback_query(F.data == "category_fast")
async def fast_food_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍕 Pizza — 35 000 so'm",
                    callback_data="product_pizza",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🍔 Burger — 25 000 so'm",
                    callback_data="product_burger",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🍟 Kartoshka fri — 15 000 so'm",
                    callback_data="product_fries",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌭 Hot-dog — 20 000 so'm",
                    callback_data="product_hotdog",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Bo'limlarga qaytish",
                    callback_data="back_categories",
                )
            ],
        ]
    )

    await callback.message.answer(
        "🍕 <b>FAST FOOD BO'LIMI</b>\n\nMahsulotni tanlang:",
        parse_mode="HTML",
        reply_markup=keyboard,
    )

    await callback.answer()


# =========================
# 🥤 ICHIMLIKLAR
# =========================


@router.callback_query(F.data == "category_drink")
async def ichimlik_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🥤 Coca-Cola — 10 000 so'm",
                    callback_data="product_cola",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🧃 Sharbat — 12 000 so'm",
                    callback_data="product_juice",
                )
            ],
            [
                InlineKeyboardButton(
                    text="☕️ Choy — 5 000 so'm", callback_data="product_tea"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Bo'limlarga qaytish",
                    callback_data="back_categories",
                )
            ],
        ]
    )

    await callback.message.answer(
        "🥤 <b>ICHIMLIKLAR BO'LIMI</b>\n\nIchimlikni tanlang:",
        parse_mode="HTML",
        reply_markup=keyboard,
    )

    await callback.answer()


# =========================
# 🍰 SHIRINLIKLAR
# =========================


@router.callback_query(F.data == "category_sweet")
async def shirinlik_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍰 Tort — 15 000 so'm", callback_data="product_cake"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🍩 Donut — 10 000 so'm",
                    callback_data="product_donut",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⬅️ Bo'limlarga qaytish",
                    callback_data="back_categories",
                )
            ],
        ]
    )

    await callback.message.answer(
        "🍰 <b>SHIRINLIKLAR BO'LIMI</b>\n\nShirinlikni tanlang:",
        parse_mode="HTML",
        reply_markup=keyboard,
    )

    await callback.answer()


# =========================
# ⬅️ BO'LIMLARGA QAYTISH
# =========================


@router.callback_query(F.data == "back_categories")
async def back_categories_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🥤 Ichimliklar", callback_data="category_drink"
                ),
                InlineKeyboardButton(
                    text="🍰 Shirinliklar", callback_data="category_sweet"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍕 Fast Food", callback_data="category_fast"
                )
            ],
        ]
    )

    await callback.message.answer(
        "👇 <b>Nima buyurtma berasiz?</b>\n\nBo'limni tanlang:",
        parse_mode="HTML",
        reply_markup=keyboard,
    )

    await callback.answer()


# =========================
# 🛒 MAHSULOTNI BUYURTMAGA QO'SHISH
# =========================

mahsulotlar = {
    "product_pizza": ("🍕 Pizza", 35000),
    "product_burger": ("🍔 Burger", 25000),
    "product_fries": ("🍟 Kartoshka fri", 15000),
    "product_hotdog": ("🌭 Hot-dog", 20000),
    "product_cola": ("🥤 Coca-Cola", 10000),
    "product_juice": ("🧃 Sharbat", 12000),
    "product_tea": ("☕️ Choy", 5000),
    "product_cake": ("🍰 Tort", 15000),
    "product_donut": ("🍩 Donut", 10000),
}


@router.callback_query(F.data.startswith("product_"))
async def product_handler(callback):
    user_id = callback.from_user.id
    mahsulot, narx = mahsulotlar[callback.data]

    if user_id not in buyurtmalar:
        buyurtmalar[user_id] = []

    buyurtmalar[user_id].append({"mahsulot": mahsulot, "narx": narx})

    await callback.message.answer(
        f"✅ <b>Buyurtmangiz qabul qilindi!</b>\n\n"
        f"🛍 <b>Mahsulot:</b> {mahsulot}\n"
        f"💰 <b>Narxi:</b> {narx:,} so'm\n\n"
        f"Buyurtmangiz <b>Buyurtmalarim</b> bo'limiga qo'shildi.",
        parse_mode="HTML",
    )

    await callback.answer("✅ Buyurtmaga qo'shildi!")


# =========================
# 🛒 BUYURTMA TUGMASI
# =========================


@router.message(F.text == "🛒 Buyurtma")
async def buyurtma_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍔 Menyudan tanlash", callback_data="back_categories"
                )
            ]
        ]
    )

    await message.answer(
        "🛒 <b>BUYURTMA BERISH</b>\n\n"
        "Menyudan o'zingizga kerakli mahsulotni tanlang 👇",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


# =========================
# 📋 BUYURTMALARIM
# =========================


@router.message(F.text == "📋 Buyurtmalar")
async def buyurtmalar_handler(message: Message):
    user_id = message.from_user.id

    if user_id not in buyurtmalar or not buyurtmalar[user_id]:
        await message.answer(
            "📋 <b>BUYURTMALARIM</b>\n\n"
            "Sizda hozircha buyurtmalar mavjud emas. 😔",
            parse_mode="HTML",
        )
        return

    matn = "📋 <b>BUYURTMALARIM</b>\n\n"
    jami = 0

    for i, buyurtma in enumerate(buyurtmalar[user_id], start=1):
        matn += (
            f"<b>{i}. {buyurtma['mahsulot']}</b>\n"
            f"💰 {buyurtma['narx']:,} so'm\n\n"
        )
        jami += buyurtma["narx"]

    matn += f"━━━━━━━━━━━━━━\n💳 <b>Jami: {jami:,} so'm</b>"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🗑 Buyurtmalarni bekor qilish",
                    callback_data="clear_cart",
                )
            ]
        ]
    )

    await message.answer(matn, parse_mode="HTML", reply_markup=keyboard)


# =========================
# 🗑 BUYURTMALARNI BEKOR QILISH
# =========================


@router.callback_query(F.data == "clear_cart")
async def clear_cart_handler(callback):
    user_id = callback.from_user.id

    if user_id in buyurtmalar:
        buyurtmalar[user_id] = []

    await callback.message.answer(
        "❌ <b>Barcha buyurtmalaringiz bekor qilindi va savat tozalandi!</b>",
        parse_mode="HTML",
    )

    await callback.answer("Buyurtmalar bekor qilindi!")


# =========================
# ℹ️ YORDAM
# =========================


@router.message(F.text == "ℹ️ Yordam")
async def yordam_button_handler(message: Message):
    await message.answer(
        "ℹ️ <b>YORDAM</b>\n\n"
        "🍔 <b>Menyu</b> — mahsulotlarni tanlash.\n"
        "🛒 <b>Buyurtma</b> — buyurtma berish.\n"
        "📋 <b>Buyurtmalar</b> — buyurtmalaringizni ko'rish va bekor qilish.\n\n"
        "✨ Yoqimli ishtaha!",
        parse_mode="HTML",
    )