from sqlalchemy import Insert, text, select, and_
from models import Base, UserInfo, LogPass, ChatPromts
from faker import Faker
from database import engine, session_factory
from sqlalchemy.orm import class_mapper

#Создает все таблицы - Для начала удаляет их всех)
def createTables():
    engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

#Генерация случайных данных для тестирования БД
def generatorBasedata():
    fake = Faker()
    registerPerson(nickname=fake.user_name(), login=fake.email(), password=fake.password())

#Регистрация нового пользователя - Одним окном будем отправлять в разные таблицы
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

#Проверка существования пользователя
def signIn(login: str, password: str):
    with session_factory() as session:
        engine.echo = False
        query = select(LogPass.id).filter(and_(LogPass.login == login, LogPass.password == password))
        if session.execute(query).all() != []:
            return True
        else:
            return False

# Обновление данных в БД
def updatePerson(id: int,
                 new_nickname: str,
                 new_rule: str,
                 new_telegramId: str,
                 new_login: str,
                 new_password: str):
    with session_factory() as session:
        engine.echo = True

        inUserInfo = session.get(UserInfo, id)
        inUserInfo.nickname = new_nickname
        inUserInfo.rule = new_rule
        inUserInfo.telegramId = new_telegramId
        session.commit()

        inLogPass = session.get(LogPass, id)
        inLogPass.login = new_login
        inLogPass.password = new_password
        session.commit()
"""
createTables()
for i in range(1, 11):
    generatorBasedata()

print("login = ")
log = input()
print("password = ")
passw = input()

res = signIn(login=log, password=passw)
print(f"Результат - {res}")

"""