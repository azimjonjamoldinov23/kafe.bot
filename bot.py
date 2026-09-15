import asyncio

from aiogram import Bot, Dispatcher

from handlers.start import router as start_router
from handlers.yordam import router as yordam_router
from handlers.tugmalar import router as tugmalar_router


TOKEN = "8987467860:AAHr-nZQqXsVF-cNsZdpeg9iSa1XJN2rwcE"


dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(yordam_router)
dp.include_router(tugmalar_router)


async def main() -> None:
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())