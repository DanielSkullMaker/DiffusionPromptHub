from sqlalchemy import Insert, text, select, and_
from models import Base, UserInfo, LogPass, ChatPromts, ElectPromts
from faker import Faker
from database import engine, session_factory
from sqlalchemy.orm import class_mapper

def createTables():
    engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def generatorBasedata():
    fake = Faker()
    registerPerson(nickname=fake.user_name(), login=fake.email(), password=fake.password())

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

def logPromt(id: int,
             promt: str):
    with session_factory() as session:
        engine.echo = True
        inChatPromts = ChatPromts(id=id, promt=promt)
        session.add(inChatPromts)
        session.commit()

def logElectPromt(nickname: str,
                  promt: str):
    with session_factory() as session:
        engine.echo = True
        inChatPromts = ElectPromts(nickname=nickname, promt=promt)
        session.add(inChatPromts)
        session.commit()

def signIn(login: str, password: str):
    with session_factory() as session:
        engine.echo = False
        query = select(LogPass.id).filter(and_(LogPass.login == login, LogPass.password == password))
        if session.execute(query).all() != []:
            query = select(UserInfo.nickname).filter(UserInfo.id == session.execute(query).all()[0][0])
            return [True, session.execute(query).all()[0][0]]
        else:
            return [False]

def getInfo(nickname: str):
    with session_factory() as session:
        engine.echo = False

        query = select(UserInfo.id, UserInfo.rule, UserInfo.created_on).filter(UserInfo.nickname == nickname)
        infoUser = session.execute(query).all()

        query = select(LogPass.login).filter(LogPass.id == infoUser[0][0])
        infoUser.append(session.execute(query).all()[0][0])

        return infoUser

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

getInfo(nickname="lol")