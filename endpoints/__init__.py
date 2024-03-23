""" Модуль конечных точек """

from flask_restx import Api
from endpoints.articles.routes import api_articles
from endpoints.categories.routes import api_categories


api = Api(
    version='1.0',
    title='Афиша',
    description='API для работы с разделами и множеством статей',
    doc='/ui'
)

api.add_namespace(api_articles)
api.add_namespace(api_categories)
