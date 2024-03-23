""" Модуль конечных точек для операций со списком статей """

from http import HTTPStatus
from flask_restx import Resource
from endpoints.articles import api_articles
from endpoints.articles.routes.marshaling import model_article, model_error
from endpoints.articles.routes.parsers import article_parser
import business.articles as articles_logic
import business.categories as categories_logic


@api_articles.route('/')
class ArticlesResource(Resource):
    """ Обрабатывает запросы на эндроинт статей """

    @api_articles.response(int(HTTPStatus.OK), 'Получен список статей', model_article)
    def get(self):
        """ Возвращает полный список всех статей """

        articles = articles_logic.get_all_articles()
        return api_articles.marshal(articles, model_article), 200

    @api_articles.expect(article_parser)
    @api_articles.response(int(HTTPStatus.CREATED), 'Создана новая статья', model_article)
    @api_articles.response(int(HTTPStatus.NOT_FOUND), 'Категория с указанными id не найдена', model_error)
    def post(self):
        """ Добавляет новую статью """

        args = article_parser.parse_args()

        category = categories_logic.get_category(args['category_id'])

        article = articles_logic.add_article(category, **args)

        return api_articles.marshal(article, model_article)
