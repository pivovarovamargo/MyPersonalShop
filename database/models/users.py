from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base

class Users(Base):
    __tablename__ = "users"# название в бд
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70))#имя пользователя mapped_column д
    telegram: Mapped[int] = mapped_column(BigInteger, unique=True)#ид в тг BigInteger - большое число, unique=True - отсутствие дубликатов
    phone: Mapped[str] = mapped_column(String, nullable=True) #стр номер телефона, String - строка, nullable=True - изначально позволяет не заполнять данные
    language: Mapped[str] = mapped_column(String(10), default="ru")

    carts: Mapped[int] = relationship("Carts", back_populates='user_cart')

    def __str__(self):
        return self.name