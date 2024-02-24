from flask_restx import Namespace, Resource, Api, reqparse

def create_parser_from_class(cls):
    parser = reqparse.RequestParser()
    for attr_name, attr_type in cls.__annotations__.items():
        parser.add_argument(attr_name, type=attr_type, help=f'{attr_name} of type {attr_type}')

    return parser