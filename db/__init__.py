from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.engine import Engine


class Base(DeclarativeBase):
    """ Базовый класс для моделей БД """


db = SQLAlchemy(model_class=Base)


# включение внешних ключей для SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
