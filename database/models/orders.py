from sqlalchemy import String, ForeignKey, DECIMAL, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class Orders(Base):
    __tablename__ = "orders"# название в бд

    id: Mapped[int] = mapped_column(primary_key=True)#уникальный номер для связи таблиц(перв. ключ)
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"))#вторичный ключ показывающий связь с перв. ключом таблицы carts(carts.id)
    product_name: Mapped[str] = mapped_column(String(50))#название - строка 50 символов
    quantity: Mapped[int]#число??
    final_price: Mapped[DECIMAL] = mapped_column(DECIMAL(10, 2))#desimal - дробная ценаб, precsion -  всего символов, scale - знаки после зпт

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)# ненулевое время создания заказа

    def __str__(self):
        return f"{self.product_name} x{self.quantity} — {self.final_price} руб"