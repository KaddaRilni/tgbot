import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router as user_router
from app.database.models import init_db

import logging

async def main():
    load_dotenv()

    await init_db()
    logging.basicConfig(level=logging.DEBUG)

    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_routers(user_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
