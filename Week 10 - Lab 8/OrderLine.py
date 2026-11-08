from product import Product, PhysicalProduct, DigitalProduct
from supplier import Supplier

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity

class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int ) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total_value = 0.0
        for order_line in self.order_lines:
            total_value += order_line.calculate_subtotal()
        
        return total_value