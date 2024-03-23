""" Модуль бизнес-логики категорий """

from db.models import db, Category


def get_category(category_id: int) -> Category:
    """ Возвращает категорию по идентификатору """

    return Category.query.get_or_404(category_id, "Категория с указанным id не найдена")


def get_all_categories() -> list[Category]:
    """ Возвращает список категорий """

    return Category.query.all()


def add_category(parent: Category = None, **kwargs) -> Category:
    """ Добавляет категорию """

    if parent is not None:
        kwargs['parent_id'] = parent.id

    new_category = Category(**kwargs)

    db.session.add(new_category)
    db.session.commit()

    return new_category


def delete_category(category_id: int) -> None:
    """ 
    Удаляет категорию по идентификатору 

    Бросает `IntegrityError`, если удаление невозможно из-за ограничений внешнего ключа
    """

    category = get_category(category_id)

    db.session.delete(category)
    db.session.commit()


def edit_category(category_id: int, **args: dict) -> None:
    """ Обновляет информацию о категории """

    category = get_category(category_id)
    category.update(**args)

    db.session.commit()
