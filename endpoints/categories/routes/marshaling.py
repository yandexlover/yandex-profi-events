""" Модели ответов для эндпоинтов категорий """

from flask_restx import fields
from endpoints.categories import api_categories

model_category = api_categories.model(
    'Категория',
    {
        'id': fields.Integer,
        'name': fields.String,
        'description': fields.String
    }
)

model_category['subCategories'] = fields.Nested(model_category)

model_error = api_categories.model(
    'Ошибка',
    {
        'message': fields.String
    }
)
