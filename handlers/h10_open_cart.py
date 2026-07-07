from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery

from database.utils import db_get_cart_items

router = Router()


@router.message(F.text == '')
async def handel_cart(message: Message):
    ''''''
    await show_cart(chat_id=message.chat.id, send_fn=message.answer)


@router.callback_query(F.text == '')
async def open_cart(callback: CallbackQuery):
    ''''''
    await show_cart(chat_id=callback.from_user.id, send_fn=callback.message.answer)
    await callback.answer()


async def show_cart(chat_id, send_fn):
    cart_items=db_get_cart_items(chat_id)
    if not cart_items:
        await send_fn('корзина пуста')
        return

    text='содержимое корзины\n'
    total=0
    for item in cart_items:
        total=float(item['final_price'])+total
        text+=f'{item['product_name']} {item['quantity']} шт. {item['final_price']} руб.\n'
    text+=f'\nИтог: {total:.2f} руб'
    await send_fn(text, reply_markup=cart_actions_kb())