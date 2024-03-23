""" Модуль с парсерами аргументов для эндпоинтов категорий """

from flask_restx.reqparse import RequestParser

category_parser = RequestParser()
category_parser.add_argument('name', required=True)
category_parser.add_argument('description', required=True)
category_parser.add_argument('parent_id', type=int)

category_edit_parser = RequestParser()
category_edit_parser.add_argument('name', location='json')
category_edit_parser.add_argument('description', location='json')
category_edit_parser.add_argument('parent_id', type=int, location='json')
