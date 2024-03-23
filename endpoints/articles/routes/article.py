""" Модуль конечных точек для операций с конкретной статьей """

from http import HTTPStatus
from flask_restx import Resource
from endpoints.articles import api_articles
from endpoints.articles.routes.marshaling import model_article, model_error
from endpoints.articles.routes.parsers import article_edit_parser
import business.articles as articles_logic
import business.categories as categories_logic


@api_articles.route('/<article_id>')
class ArticleResource(Resource):
    """ Обрабатывает запросы на эндроинт конкретной статьи """

    @api_articles.response(int(HTTPStatus.OK), 'Получена информация о статье', model_article)
    @api_articles.response(int(HTTPStatus.NOT_FOUND), 'Статья с указанными идентификатором не существует', model_error)
    def get(self, article_id: int):
        """ Возвращает информацию о конкретной статье с идентификатором <article_id> """

        article = articles_logic.get_article(article_id)

        return api_articles.marshal(article, model_article), HTTPStatus.OK

    @api_articles.expect(article_edit_parser)
    @api_articles.response(int(HTTPStatus.NO_CONTENT), 'Статья отредактирована')
    @api_articles.response(int(HTTPStatus.NOT_FOUND), 'Редактируемая статья или указанная категория не найдены', model_error)
    def put(self, article_id: int):
        """ Обновляет информацию о статье с идентификатором <article_id> """

        args = article_edit_parser.parse_args()
        args = dict(filter(lambda x: x[1] is not None, args.items()))

        category_id = args.get('category_id', None)
        if category_id is not None:
            categories_logic.get_category(category_id)

        articles_logic.edit_article(article_id, **args)

        return None, HTTPStatus.NO_CONTENT
