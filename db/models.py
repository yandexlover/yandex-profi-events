from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db import db


class BaseModel(db.Model):
    """ Базовый класс модели данных БД """

    __abstract__ = True


class Article(BaseModel):
    """ Модель данных статьи """

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('category.id', ondelete='RESTRICT')
    )


class Category(BaseModel):
    """ Модель данных категории """

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    parent_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('category.id', ondelete='RESTRICT'),
        nullable=True
    )

    subCategories: Mapped[list['Category']] = db.relationship(
        'Category',
        passive_deletes=True
    )
