from flask_restx import Namespace

api_categories = Namespace(
    'Категории', 'Операции с категориями', '/categories')
