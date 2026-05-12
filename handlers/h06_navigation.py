from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message
from aiogram import Router, F, Bot

from handlers.h03_order import handle_main_menu


router=Router()
@router.messege(F.text == '<= назад')
async def back_to_category(message: Message, bot: Bot):
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except TelegramBadRequest:
        pass

    await handle_main_menu(message, bot)