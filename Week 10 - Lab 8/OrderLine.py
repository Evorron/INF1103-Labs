from Product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product.__price * self.quantity