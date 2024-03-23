from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db import Base


class Article(Base):
    """ Модель данных статьи """

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('category.id', ondelete='RESTRICT')
    )


class Category(Base):
    """ Модель данных категории """

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    parent_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('category.id', ondelete='RESTRICT')
    )
