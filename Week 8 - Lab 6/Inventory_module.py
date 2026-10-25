from product_module import Product

class Inventory():

    def __init__(self):
        self.__inventory = []       #Empty inventory list attribute

    def add_product(self, product):
        self.__inventory.append(product)

    def search_product(self, product_id_name):
        for product in self.__inventory:
            if product.get_name().lower() == product_id_name.lower() or product.get_id().lower() == product_id_name.lower():
                print("\nProduct Found")
    
                return product

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")
    
        for product in self.__inventory:
            product.display_information()
    
        print("------------------------------------------------")

    # Getter method for list
    def get_inventory(self):
        return self.__inventory