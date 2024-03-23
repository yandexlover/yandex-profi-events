""" Модели ответов для эндпоинтов статей """

from flask_restx import fields
from endpoints.articles import api_articles

model_article = api_articles.model(
    'Статья',
    {
        'id': fields.Integer,
        'name': fields.String,
        'description': fields.String,
        'category_id': fields.Integer
    }
)

model_error = api_articles.model(
    'Ошибка',
    {
        'message': fields.String
    }
)
