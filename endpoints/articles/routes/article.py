""" Модуль конечных точек для операций с конкретной статьей """

from flask_restx import Resource
from endpoints.articles import api_articles


@api_articles.route('/<article_id>')
class ArticleResource(Resource):
    """ Обрабатывает запросы на эндроинт конкретной статьи """

    def get(self, article_id):
        """ Возвращает информацию о конкретной статье с идентификатором <article_id> """
        return {'id': article_id}
