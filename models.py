from sqlalchemy import Integer, String,\
    Column, DateTime, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base, Mapped, mapped_column,\
    relationship
from datetime import datetime

Base = declarative_base()

class LogPass(Base):
    """
        #id пользователя
        id = Column(Integer, ForeignKey('UserInfo.id'))

        #Логин и пароль
        login = Column(String(50), nullable=False)
        password = Column(String(50), nullable=False)
    """
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
    """
        #Id, имя и роль пользователя
        id = Column(Integer, primary_key=True)
        nickname = Column(String(50), nullable=False)
        rule = Column(String(50), default="Nope")

        #Дата создания аккаунта
        created_on = Column(DateTime(), default=datetime.now),

        #Id телеги для бота (возможного)
        telegramId = Column(String(50), nullable=True)
    """
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
    """
        #id, время, и запрос в api модели
        id = Column(Integer, ForeignKey('UserInfo.id'))
        datetime = Column(DateTime(), default=datetime.now)
        promt = Column(String(200), nullable=False)
    """
    __tablename__ = 'ChatProms'

    id: Mapped[int] = mapped_column(ForeignKey('UserInfo.id'))
    datetime: Mapped[str] = mapped_column(default=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    promt: Mapped[str] = mapped_column(nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
    )