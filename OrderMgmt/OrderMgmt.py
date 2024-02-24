from flask import json, request
#from flask_restful import Resource
from flask_restx import Namespace, Resource, Api
from Order import Order

from Product import Product
from User import User
from Route import order_routes

order_ns = Namespace('OrderManagement APIs', description='Order Manager Operations')
orderModule = order_ns.model('Order', Order)

@order_ns.route('/')
class OrderMgmt(Resource):
    ords=[]

    # @order_ns.route('/GetOrderDetails/<int:orderid>', methods=['GET']) 
    # def GetOrderDetails(self, orderid):
    #     return {'Orders': ords[orderid]}

    # @order_ns.route('/GetAllOrders', methods=['GET']) 
    # def GetAllOrders(self):
    #     return {'Orders': ords}

    @order_ns.doc('/') 
    #@order_ns.marshal_list_with(Order) 
    def get(self):
        return {'Orders': self.ords}
    
    def put(self):
        ord = request.get_json()
        self.ords.append(ord)
        return {'Orders': self.ords}
    
    def delete(self):
        self.ords.clear()
        return {'Orders': self.ords}