from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from keyboards.inliine import generate_category_menu

router=Router()

@router.callback_query(F.data.regexp(r'^category_(\d+)$'))
async def schow_product(callback: CallbackQuery):
    '''думонстрация всех продуктов выбраной котегории'''
    chat_id=callback.message.chat.id
    messege_id=callback.message.message_id
    category_id=int(callback.data.split('_')[-1])
    try:
        await callback.bot.edit_messege_text(
            text='выбери продукт',
            chat_id=chat_id,
            message_id=messege_id,
            reply_markup=show_product_by_category(category_id)
        )
    except TelegramBadRequest:
        await callback.answer('не удалось открыть категорию')

@router.callback_query(F.data=='return_to_category')
async def return_to_category(callback: CallbackQuery):#callback экземпляр класса CallbackQuery
    '''возврат к спику категорий'''
    chat_id=callback.message.chat.id
    messege_id=callback.message.message_id

    await callback.bot.edit_message_text(
        text='вибери категорию'
        chat_id = chat_id,
        message_id = messege_id,
        reply_markup=generate_category_menu(chat_id)
    )