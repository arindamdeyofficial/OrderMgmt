
from typing import List
from Product import Product


class Order:
    def __init__(self, order_id: int, products: list, total_amount: int, customer_name: str, shipping_address: str):
        self.order_id = order_id
        self.products = products
        self.total_amount = total_amount
        self.customer_name = customer_name
        self.shipping_address = shipping_address

    def display_order_info(self):
        print(f"Order ID: {self.order_id}")
        print("Products:")
        for product in self.products:
            print(f"  - {product}")
        print(f"Total Amount: ${self.total_amount}")
        print(f"Customer: {self.customer_name}")
        print(f"Shipping Address: {self.shipping_address}")

class SampleClass:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")