""" Модуль с парсерами аргументов для эндпоинтов статей """

from flask_restx.reqparse import RequestParser

article_parser = RequestParser()
article_parser.add_argument('name', required=True)
article_parser.add_argument('description', required=True)
article_parser.add_argument('category_id', type=int, required=True)

article_edit_parser = RequestParser()
article_edit_parser.add_argument('name', location='json')
article_edit_parser.add_argument('description', location='json')
article_edit_parser.add_argument('category_id', type=int, location='json')
