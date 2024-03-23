""" Модуль с парсерами аргументов для эндпоинтов категорий """

from flask_restx.reqparse import RequestParser

category_parser = RequestParser()
category_parser.add_argument('name', required=True)
category_parser.add_argument('description', required=True)
category_parser.add_argument('parent_id', type=int)
