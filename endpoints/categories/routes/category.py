""" Модуль конечных точек для операций с конкретной категорией """

from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask_restx import Resource, abort
from endpoints.categories import api_categories
from endpoints.categories.routes.marshaling import model_category, model_error
from endpoints.categories.routes.parsers import category_edit_parser
import business.categories as categories_logic


@api_categories.route('/<category_id>')
class CategoryResource(Resource):
    """ Обрабатывает запросы на эндроинт конкретной категории """

    @api_categories.response(int(HTTPStatus.OK), 'Получена информация о категории', model_category)
    @api_categories.response(int(HTTPStatus.NOT_FOUND), 'Категория с указанным идентификатором не существует', model_error)
    def get(self, category_id: int):
        """ Возвращает информацию о конкретной категории с идентификатором <category_id> """

        category = categories_logic.get_category(category_id)

        return api_categories.marshal(category, model_category), HTTPStatus.OK

    @api_categories.response(int(HTTPStatus.NO_CONTENT), 'Удалена категория')
    @api_categories.response(int(HTTPStatus.NOT_FOUND), 'Категория с указанным идентификатором не существует', model_error)
    @api_categories.response(int(HTTPStatus.CONFLICT), 'Категория имеет связанные подкатегории или статьи', model_error)
    def delete(self, category_id: int):
        """ Удаляет категорию с идентификатором <category_id> """

        try:
            categories_logic.delete_category(category_id)
        except IntegrityError:
            abort(
                HTTPStatus.CONFLICT,
                'Категория имеет связанные подкатегории или статьи'
            )

        return None, HTTPStatus.NO_CONTENT

    @api_categories.expect(category_edit_parser)
    @api_categories.response(int(HTTPStatus.NO_CONTENT), 'Статья отредактирована')
    @api_categories.response(int(HTTPStatus.NOT_FOUND), 'Редактируемая статья или указанная категория не найдены', model_error)
    def put(self, category_id: int):
        """ Обновляет информацию о статье с идентификатором <category_id> """

        args = category_edit_parser.parse_args()
        args = dict(filter(lambda x: x[1] is not None, args.items()))

        parent_id = args.get('parent_id', None)
        if parent_id is not None:
            categories_logic.get_category(parent_id)

        categories_logic.edit_category(category_id, **args)

        return None, HTTPStatus.NO_CONTENT
