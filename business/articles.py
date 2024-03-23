""" Модуль бизнес-логики статей """

from db.models import db, Article, Category


def get_article(article_id) -> Article:
    """ Возвращает статью по идентификатору """

    return Article.query.get_or_404(article_id, "Статья с указанным id не найдена")


def get_all_articles() -> list[Article]:
    """ Возвращает список статей """

    return Article.query.all()


def add_article(category: Category, **kwargs) -> Article:
    """ Добавляет статью """

    kwargs['category_id'] = category.id
    new_article = Article(**kwargs)

    db.session.add(new_article)
    db.session.commit()

    return new_article


def delete_article(article_id: int) -> None:
    """ Удалает статью по идентификатору """

    article = get_article(article_id)

    db.session.delete(article)
    db.session.commit()
