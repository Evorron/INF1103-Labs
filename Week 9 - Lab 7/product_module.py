class Product:

    def __init__(self, id, name, price, quantity):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def update_stock(self, new_quantity):
        if new_quantity >= 0:
            self.__quantity = new_quantity

    def display_information(self):
        print(f"ID: {self.__id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__quantity}", end="")

    # Getter method to retrieve product details
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity


class PhysicalProduct(Product):
    def __init__(self, id, name, price, quantity, weight):
        super().__init__(id, name, price, quantity)
        self.__weight = weight

    # Overwrites Product method display_information()
    def display_information(self):
            super().display_information()
            print(f" | Weight: {self.__weight}")

class DigitalProduct(Product):
    def __init__(self, id, name, price, quantity, download_size):
        super().__init__(id, name, price, quantity)
        self.__download_size = download_size

    # Overwrites Product method display_information()
    def display_information(self):
            super().display_information()
            print(f" | Download Size: {self.__download_size}")


physical = PhysicalProduct("P100", "Mouse", 150, 10, 10)
digital = DigitalProduct("P101", "MS", 80, 1000, 2500)

physical.display_information()
digital.display_information()