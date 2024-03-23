""" Модуль конечных точек для операций с конкретной статьей """

from http import HTTPStatus
from flask_restx import Resource
from endpoints.articles import api_articles
from endpoints.articles.routes.marshaling import model_article, model_error
from business.articles import get_article


@api_articles.route('/<article_id>')
class ArticleResource(Resource):
    """ Обрабатывает запросы на эндроинт конкретной статьи """

    @api_articles.response(int(HTTPStatus.OK), 'Получена информация о статье', model_article)
    @api_articles.response(int(HTTPStatus.NOT_FOUND), 'Статья с указанными идентификатором не существует', model_error)
    def get(self, article_id: int):
        """ Возвращает информацию о конкретной статье с идентификатором <article_id> """

        article = get_article(article_id)

        return api_articles.marshal(model_article, article), 200
