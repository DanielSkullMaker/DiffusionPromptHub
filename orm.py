from sqlalchemy import Insert, text
from models import Base
from models import UserInfo, LogPass, ChatPromts
from database import engine, session_factory
from sqlalchemy.orm import class_mapper

#Создает все таблицы - Для начала удаляет их всех)
def createTables():
    engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

#Регистрация нового пользователя
#Одним окном будем отправлять в разные таблицы
def registerPerson(nickname: str,
                   login: str,
                   password: str):
    with session_factory() as session:
        engine.echo = False
        inUserInfo = UserInfo(nickname=nickname)
        session.add(inUserInfo)
        session.commit()

        inLogPass = LogPass(id=inUserInfo.id, login=login, password=password)
        session.add(inLogPass)
        session.commit()

#Добавление промта в БД
def LogPromt(id: int,
             promt: str):
    with session_factory() as session:
        engine.echo = True
        inChatPromts = ChatPromts(id=id, promt=promt)
        session.add(inChatPromts)
        session.commit()

"""
createTables()

Nick = "TestNick1"
Log = "xxxx@xx.com"
Pass = "000000f"

registerPerson(nickname = Nick,
                login = Log,
                password = Pass)
"""


