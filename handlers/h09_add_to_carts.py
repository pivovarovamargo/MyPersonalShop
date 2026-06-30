from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from database.utils import db_get_user_cart, db_get_product_by_name, db_add_or_update_item
from handlers.h06_navigation import back_to_category
from main import bot

router = Router()


@router.callback_query(F.data == 'в корзину')
async def put_in_cart(callback: CallbackQuery):
    '''добавление товара в корзину'''
    chat_id = callback.message.chat_id
    message = callback.message
    caption = message.caption
    if not caption:
        await bot.send_messege(chat_id=chat_id, text='')
        return

    product_name = caption.split('\n')[0]
    cart = db_get_user_cart(chat_id)
    if not cart:
        await bot.send_message(chat_id=chat_id, text='')
        return
    product = db_get_product_by_name(product_name)
    result = db_add_or_update_item(
        cart_id=cart.id,
        product_id=product.id,
        product_name=product_name,
        product_price=product.price,
        increment=0,
    )
    try:
        await bot_delete_message(chat_id=chat_id, message_id=message.id+1)
    except:
        pass
    try:
        await bot_delete_message(chat_id=chat_id, message_id=message.id)
    except:
        pass
    if result['status']=='ok':
        await bot.send_message(chat_id=chat_id, text='добавлен')
    else:
        await bot.send_message(chat_id=chat_id, text='ошибка')
    await back_to_category(message, bot)