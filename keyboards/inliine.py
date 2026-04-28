from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.models.products import Products
from database.utils import db_get_finally_price, db_get_all_category, get_session


def generate_category_menu(chat_id):
    """создание инлайн клавиатуры с категориями продуктов"""
    categories = db_get_all_category()
    total_price = db_get_finally_price(chat_id)

    builder = InlineKeyboardBuilder()
    builder.button(
        text=f'Корзина заказа ({total_price if total_price else 0} рублей)',
        callback_data='Корзина заказа'
    )
    [builder.button(text=category.category_name, callback_data=f'category_{category.id}')
     for category in categories]

    builder.adjust(1, 2)
    return builder.as_markup()
def show_product_by_category(category_id: int):
    """кнопка для показа продуктов по категориям"""
    products = db_get_product(category_id)
    builder = InlineKeyboardBuilder()
    [builder.button(text=product.product_name, callback_data=f'product_view_{product.id}') for product in products]
    builder.adjust(2)
    builder.row(
    InlineKeyboardButton(text="⬅ Назад", callback_data='return_to_category')
    )
    return builder.as_markup()
def db_get_product(category_id):
    with get_session() as session:
        query = select(Products).where(Products.category_id == category_id)