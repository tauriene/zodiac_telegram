__all__ = ('router', )

from aiogram import Router
from .user import router as user_router

router = Router()
router.include_routers(user_router)