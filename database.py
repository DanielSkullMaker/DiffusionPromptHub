from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(
    url=settings.DatabaseURL_psycopg,
    echo=False,
    #pool_size=5 #Кол-во подключений к базе данных
    #max_overflow=10, #Доп. подключения
)

session_factory = sessionmaker(engine)
