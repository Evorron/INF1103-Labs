from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, id: str, name: str, price: float, quantity: int, supplier: Supplier):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.supplier: Supplier = supplier

    @abstractmethod
    def get_fulfilment_info(self) -> None:
         pass

    def update_stock(self, new_quantity) -> None:
        if new_quantity >= 0:
            self.__quantity = new_quantity

    def display_information(self) -> None:
        print(f"ID: {self.__id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__quantity}", end="")

    # Getter method to retrieve product details
    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_quantity(self) -> int:
        return self.__quantity

# Interface 
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """
        Child Classes created must override this method
        """
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, id: str, name: str, price: float, quantity: int, weight: float, supplier: Supplier):
        super().__init__(id, name, price, quantity, supplier)
        self.__weight = weight

    # Overwrites Product method display_information()
    def display_information(self) -> None:
        super().display_information()
        print(f" | Weight(kg): {self.__weight}")

    def get_fulfilment_info(self) -> None:
        print("This product requires physical shipping")

    def calculate_shipping_cost(self) -> float:
        return (self.__weight * 2.00) + (self.get_price() * 0.01)

    def get_type(self) -> str:
        return "Physical"

    def get_add_info(self) -> float:
        return self.__weight

class DigitalProduct(Product):
    def __init__(self, id, name: str, price: float, quantity: int, download_size: float, supplier: Supplier):
        super().__init__(id, name, price, quantity, supplier)
        self.__download_size = download_size

    # Overwrites Product method display_information()
    def display_information(self) -> None:
        super().display_information()
        print(f" | Download Size(Gb): {self.__download_size}")

    def get_fulfilment_info(self) -> None:
            print("This product is delivered digitally via download")

    def get_type(self) -> str:
        return "Digital"

    def get_add_info(self) -> float:
        return self.__download_size