""" Модуль конечных точек для операций со списком категорий """

from http import HTTPStatus
from flask_restx import Resource
from endpoints.categories import api_categories
from endpoints.categories.routes.marshaling import model_category, model_error
from endpoints.categories.routes.parsers import category_parser
import business.articles as articles_logic
import business.categories as categories_logic


@api_categories.route('/')
class CategoriesResource(Resource):
    """ Обрабатывает запросы на эндроинт категорий """

    @api_categories.response(int(HTTPStatus.OK), 'Получен список категорий', model_category)
    def get(self):
        """ Возвращает полный список всех категорий """

        categories = categories_logic.get_all_categories()
        return api_categories.marshal(categories, model_category), 200

    @api_categories.expect(category_parser)
    @api_categories.response(int(HTTPStatus.CREATED), 'Создана новая категория', model_category)
    @api_categories.response(int(HTTPStatus.NOT_FOUND), 'Родительская категория с указанными id не найдена', model_error)
    def post(self):
        """ Добавляет новую категорию """

        args = category_parser.parse_args()

        parent = None
        parent_id = args.get('parent_id')

        if parent_id is not None:
            parent = categories_logic.get_category(parent_id)
            print(parent.id)

        category = categories_logic.add_category(parent, **args)

        return api_categories.marshal(category, model_category)
