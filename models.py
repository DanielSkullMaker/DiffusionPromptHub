from sqlalchemy import Integer, String, Column, DateTime, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from datetime import datetime

Base = declarative_base()

class LogPass(Base):
    __tablename__ = 'LogPass'

    id: Mapped[int] = mapped_column(ForeignKey('UserInfo.id'))
    login: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    __table_args__ = (
        #Установка на уникальный логин
        UniqueConstraint('login'), # Запятую не удалять - ошибка типа данных будет

        #В таблице не может быть двух первичных ключей. Вместо этого вы должны использовать составной первичный ключ
        #  -Stack Overflow
        PrimaryKeyConstraint('id')
    )

class UserInfo(Base):
    __tablename__ = "UserInfo"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(nullable=False)
    rule: Mapped[str] = mapped_column(default="Nope")
    created_on: Mapped[str] = mapped_column(default=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    telegramId: Mapped[str] = mapped_column(nullable=True)

    __table_args__ = (
        # Установка на уникальное имя
        UniqueConstraint('nickname'),
    )

class ChatPromts(Base):
    __tablename__ = 'ChatProms'

    id: Mapped[int] = mapped_column(ForeignKey('UserInfo.id'))
    datetime: Mapped[str] = mapped_column(default=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    promt: Mapped[str] = mapped_column(nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )

class ElectPromts(Base):
    __tablename__ = 'ElectPromts'

    id_promt: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(nullable=False)
    promt: Mapped[str] = mapped_column(nullable=False)