class Order:
    def __init__(self, order_id, products, total_amount, customer_name, shipping_address):
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