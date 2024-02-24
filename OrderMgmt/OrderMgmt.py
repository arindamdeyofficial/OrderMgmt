import asyncio
from attr import fields
from flask import Response, json, request
#from flask_restful import Resource
from flask_restx import Namespace, Resource, Api, reqparse
from Order import Order
from OrderParser import create_parser_from_class

from Product import Product
from User import User
from Route import order_routes

order_ns = Namespace('OrderManagement APIs', description='Order Manager Operations')
orderModule = order_ns.model('Order', {'description': fields.__str__})

order_parser = create_parser_from_class(Order)

@order_ns.route('/')
class OrderMgmt(Resource):
    ords=[]
     
    def get(self) -> list[Order]:
        #await asyncio.sleep(2)
        return {'Orders': self.ords}
    
    @order_ns.expect(order_parser)
    def put(self):
        ord = request.get_json()
        self.ords.append(ord)
        return {'Orders': self.ords}
    
    @order_ns.expect(order_parser)
    def post(self):
        ord = request.get_json()
        self.ords.append(ord)
        return {'Orders': self.ords}
    
    def delete(self):
        self.ords.clear()
        return {'Orders': self.ords}