from aiogram import F, Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

router = Router()

fast_food = {
    "🍕 Pizza": 35000,
    "🍔 Burger": 25000,
    "🍟 Kartoshka fri": 15000,
    "🌭 Hot-dog": 20000,
    "Lavash": 28000,
    "🌮 Svinich": 22000,
    "🧆 Naggetslar": 18000,
}

issiq_taomlar = {
    "🍜 Lag'mon": 28000,
    "🍲 Sho'rva": 25000,
    "🍚 Osh (Palov)": 30000,
    "🧆 Somsa": 8000,
}

ichimliklar = {
    "🥤 Coca-Cola 1.5L": 14000,
    "🥤 Fanta 1.5L": 14000,
    "🧃 Tabiiy Sharbat": 15000,
    "☕️ Amerikano": 12000,
    "☕️ Kapuchino": 15000,
    "🫖 Limonli choy": 7000,
}

shirinliklar = {
    "🍰 Snikers tort": 20000,
    "🍰 Chizkeyk": 22000,
    "🍩 Shokoladli Donut": 12000,
    "🍦 Muzqaymoq": 10000,
}

buyurtmalar = {}


@router.message(F.text == "🍔 Menyu")
async def menyu_handler(message: Message):
    menyu_matni = (
        "📜 <b>KAFE MENYUSI</b>\n\n"
        "🍕 <b>Fast food:</b>\n"
        "• Pizza — 35 000 so'm\n"
        "• Burger — 25 000 so'm\n"
        "• Kartoshka fri — 15 000 so'm\n"
        "• Hot-dog — 20 000 so'm\n"
        "• Lavash — 28 000 so'm\n"
        "• Sendvich — 22 000 so'm\n"
        "• Naggetslar — 18 000 so'm\n\n"
        "🍲 <b>Issiq taomlar:</b>\n"
        "• Lag'mon — 28 000 so'm\n"
        "• Sho'rva — 25 000 so'm\n"
        "• Osh (Palov) — 30 000 so'm\n"
        "• Somsa — 8 000 so'm\n\n"
        "🥤 <b>Ichimliklar:</b>\n"
        "• Coca-Cola 1.5L — 14 000 so'm\n"
        "• Fanta 1.5L — 14 000 so'm\n"
        "• Tabiiy Sharbat — 15 000 so'm\n"
        "• Amerikano — 12 000 so'm\n"
        "• Kapuchino — 15 000 so'm\n"
        "• Limonli choy — 7 000 so'm\n\n"
        "🍰 <b>Shirinliklar:</b>\n"
        "• Snikers tort — 20 000 so'm\n"
        "• Chizkeyk — 22 000 so'm\n"
        "• Shokoladli Donut — 12 000 so'm\n"
        "• Muzqaymoq — 10 000 so'm"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍕 Fast Food", callback_data="category_fast"
                ),
                InlineKeyboardButton(
                    text="🍲 Issiq taomlar", callback_data="category_hot"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥤 Ichimliklar", callback_data="category_drink"
                ),
                InlineKeyboardButton(
                    text="🍰 Shirinliklar", callback_data="category_sweet"
                ),
            ],
        ]
    )

    await message.answer(menyu_matni, parse_mode="HTML")
    await message.answer(
        "👇 <b>Nima buyurtma berasiz?</b>\n\nBo'limni tanlang:",
        parse_mode="HTML",
        reply_markup=keyboard,
    )


@router.callback_query(F.data == "category_fast")
async def fast_food_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍕 Pizza — 35 000", callback_data="product_pizza"
                ),
                InlineKeyboardButton(
                    text="🍔 Burger — 25 000", callback_data="product_burger"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍟 Kartoshka fri — 15 000",
                    callback_data="product_fries",
                ),
                InlineKeyboardButton(
                    text="🌭 Hot-dog — 20 000", callback_data="product_hotdog"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🌯 Lavash — 28 000", callback_data="product_lavash"
                ),
                InlineKeyboardButton(
                    text="🌮 Sendvich — 22 000",
                    callback_data="product_sandwich",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🧆 Naggetslar — 18 000",
                    callback_data="product_nuggets",
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


@router.callback_query(F.data == "category_hot")
async def hot_food_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍜 Lag'mon — 28 000", callback_data="product_lagmon"
                ),
                InlineKeyboardButton(
                    text="🍲 Sho'rva — 25 000", callback_data="product_shorva"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍚 Osh — 30 000", callback_data="product_osh"
                ),
                InlineKeyboardButton(
                    text="🧆 Somsa — 8 000", callback_data="product_somsa"
                ),
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
        "🍲 <b>ISSIQ TAOMLAR BO'LIMI</b>\n\nTaomni tanlang:",
        parse_mode="HTML",
        reply_markup=keyboard,
    )
    await callback.answer()


@router.callback_query(F.data == "category_drink")
async def ichimlik_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🥤 Coca-Cola — 14 000", callback_data="product_cola"
                ),
                InlineKeyboardButton(
                    text="🥤 Fanta — 14 000", callback_data="product_fanta"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🧃 Sharbat — 15 000", callback_data="product_juice"
                ),
                InlineKeyboardButton(
                    text="🫖 Limon choy — 7 000", callback_data="product_tea"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☕️ Amerikano — 12 000",
                    callback_data="product_americano",
                ),
                InlineKeyboardButton(
                    text="☕️ Kapuchino — 15 000",
                    callback_data="product_cappuccino",
                ),
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


@router.callback_query(F.data == "category_sweet")
async def shirinlik_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍰 Snikers tort — 20 000",
                    callback_data="product_snikers",
                ),
                InlineKeyboardButton(
                    text="🍰 Chizkeyk — 22 000",
                    callback_data="product_cheesecake",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🍩 Donut — 12 000", callback_data="product_donut"
                ),
                InlineKeyboardButton(
                    text="🍦 Muzqaymoq — 10 000",
                    callback_data="product_icecream",
                ),
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


@router.callback_query(F.data == "back_categories")
async def back_categories_handler(callback):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🍕 Fast Food", callback_data="category_fast"
                ),
                InlineKeyboardButton(
                    text="🍲 Issiq taomlar", callback_data="category_hot"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥤 Ichimliklar", callback_data="category_drink"
                ),
                InlineKeyboardButton(
                    text="🍰 Shirinliklar", callback_data="category_sweet"
                ),
            ],
        ]
    )

    await callback.message.answer(
        "👇 <b>Nima buyurtma berasiz?</b>\n\nBo'limni tanlang:",
        parse_mode="HTML",
        reply_markup=keyboard,
    )
    await callback.answer()


mahsulotlar = {
    "product_pizza": ("🍕 Pizza", 35000),
    "product_burger": ("🍔 Burger", 25000),
    "product_fries": ("🍟 Kartoshka fri", 15000),
    "product_hotdog": ("🌭 Hot-dog", 20000),
    "product_lavash": ("🌯 Lavash", 28000),
    "product_sandwich": ("🌮 Sendvich", 22000),
    "product_nuggets": ("🧆 Naggetslar", 18000),
    "product_lagmon": ("🍜 Lag'mon", 28000),
    "product_shorva": ("🍲 Sho'rva", 25000),
    "product_osh": ("🍚 Osh (Palov)", 30000),
    "product_somsa": ("🧆 Somsa", 8000),
    "product_cola": ("🥤 Coca-Cola 1.5L", 14000),
    "product_fanta": ("🥤 Fanta 1.5L", 14000),
    "product_juice": ("🧃 Tabiiy Sharbat", 15000),
    "product_tea": ("🫖 Limonli choy", 7000),
    "product_americano": ("☕️ Amerikano", 12000),
    "product_cappuccino": ("☕️ Kapuchino", 15000),
    "product_snikers": ("🍰 Snikers tort", 20000),
    "product_cheesecake": ("🍰 Chizkeyk", 22000),
    "product_donut": ("🍩 Shokoladli Donut", 12000),
    "product_icecream": ("🍦 Muzqaymoq", 10000),
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
        f"Buyurtmangiz <b>Buyurtmalar</b> bo'limiga qo'shildi.",
        parse_mode="HTML",
    )
    await callback.answer("✅ Buyurtmaga qo'shildi!")


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