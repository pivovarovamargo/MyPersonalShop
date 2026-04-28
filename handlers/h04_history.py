from aiogram.types import Message
from aiogram import Router, F

from database.utils import db_get_last_orders

router = Router()


@router.message(F.text == "📒 История")
async def show_order_history(message: Message):
    '''последние 5 позиций заказа'''
    chat_id = message.chat.id
    orders = db_get_last_orders(chat_id)
    if not orders:
        await message.answer('нема')
        return

    text = "5 заказов"
    for item in orders:
        order = item['order']
        line_prise = float(order.final_price)
        text += f'{order.product_name} {order.quantity} {line_prise:..2f} руб'

    await message.answer(text)
