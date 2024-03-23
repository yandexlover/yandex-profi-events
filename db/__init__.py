""" Модуль для операций с БД """

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.engine import Engine


# class Base(DeclarativeBase):
#     """ Базовый класс для моделей БД """


db = SQLAlchemy()


# включение внешних ключей для SQLite при подключении к БД
# pylint:disable = unused-argument
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """ Включает использование внешних ключей в SQLite БД """

    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
