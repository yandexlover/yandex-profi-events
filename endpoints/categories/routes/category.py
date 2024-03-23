""" Модуль конечных точек для операций с конкретной категорией """

from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask_restx import Resource, abort
from endpoints.categories import api_categories
from endpoints.categories.routes.marshaling import model_category, model_error
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

    @api_categories.response(int(HTTPStatus.OK), 'Удалена категория')
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

        return {'success': True}, HTTPStatus.OK
