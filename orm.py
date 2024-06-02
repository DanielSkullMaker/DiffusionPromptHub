from sqlalchemy import Insert, text, select, delete, and_
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

def logPromt(nickname: str,
             promt: str):
    with session_factory() as session:
        engine.echo = False
        query = select(UserInfo.id).filter(UserInfo.nickname == nickname)
        inChatPromts = ChatPromts(id_person=session.execute(query).all()[0][0], promt=promt)
        session.add(inChatPromts)
        session.commit()

def logElectPromt(id: int):
    with session_factory() as session:
        engine.echo = True

        query = select(ChatPromts.promt).filter(ChatPromts.id == id)
        inElectPromts = ElectPromts(id_promt=id, promt=session.execute(query).all()[0][0])
        session.add(inElectPromts)

        obj = session.query(ChatPromts).filter(ChatPromts.id == id).first()
        session.delete(obj)

        """
        deletePromt = delete(ChatPromts).filter(ChatPromts.id == id)
        session.add(deletePromt)
        """
        session.commit()

def signIn(login: str, password: str):
    with session_factory() as session:
        engine.echo = False
        query = select(LogPass.id).filter(and_(LogPass.login == login, LogPass.password == password))
        if session.execute(query).all() != []:
            query = select(UserInfo.nickname, UserInfo.rule).filter(UserInfo.id == session.execute(query).all()[0][0])
            return [True, session.execute(query).all()[0][0], session.execute(query).all()[0][1]]
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

def getAllInfo():
    with session_factory() as session:
        query = select(UserInfo.id, UserInfo.nickname, UserInfo.rule, UserInfo.created_on)
        return session.execute(query).all()

def getAllPromt():
    with session_factory() as session:
        query = select(ChatPromts.id, ChatPromts.id_person, ChatPromts.datetime, ChatPromts.promt)
        return session.execute(query).all()

def getAllElectPromt():
    with session_factory() as session:
        query = select(ElectPromts.id_promt, ElectPromts.created_on, ElectPromts.promt)
        return session.execute(query).all()

def postRule(id: int, rule: str):
    with session_factory() as session:
        engine.echo = True
        inUserInfo = session.get(UserInfo, id)
        inUserInfo.rule = rule
        session.commit()

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