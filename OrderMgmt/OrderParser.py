from typing import get_type_hints
from flask_restx import Namespace, Resource, Api, reqparse

def create_parser_from_class(cls):
    print(get_type_hints(cls.__init__))
    parser = reqparse.RequestParser()
    for attr_name, attr_type in get_type_hints(cls.__init__).items():
        print(attr_name)
        parser.add_argument(attr_name, type=attr_type, help=f'{attr_name} of type {attr_type}')
    
    return parser