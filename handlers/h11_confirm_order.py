from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from database.utils import db_get_user_phone

router = Router()


@router.callback_query(F.data == 'confirm_order')
async def confirm_order(callback: CallbackQuery, bot: Bot):
    '''оформление заказа'''
    user = callback.from_user
    phone = db_get_user_phone(user.id)