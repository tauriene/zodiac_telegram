import asyncio

import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.utils import settings
from src.handlers import router as main_router




async def bot_startup(bot: Bot):
    await bot.send_message(settings.admin_id, "The bot has started.")


async def bot_shutdown(bot: Bot):
    await bot.send_message(settings.admin_id, "The bot has shut down.")


async def main():
    load_dotenv()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - "
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )

    logger = logging.getLogger(__name__)

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )
    dp = Dispatcher()

    dp.startup.register(bot_startup)
    dp.shutdown.register(bot_shutdown)

    dp.include_router(main_router)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error("An error occurred: %s" % e)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
