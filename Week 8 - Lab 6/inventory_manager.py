# Imports
import json

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
        print(f"ID: {self.__id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__quantity}")

    # Getter method to retrieve product details
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

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


# Menu
def menu_system():
   print("\n----------- MENU -----------")
   print("1. Display All Products")
   print("2. Add Product")
   print("3. Update Stock")
   print("4. Search Product")
   print("5. Save Inventory")
   print("6. Exit")
   print("-----------------------------\n")

   option = input("Enter option: ")
   print("")

   if option.isdigit():
       return int(option)
   else:
       print("Enter a valid option")

def add_product():
# Prompts and retrieves user input
    while True:
        print("Add New Product")
        product_id = input("Product ID (e.g. PXXX): ")
        
        # Checks invalid inputs
        if product_id.isdigit() or product_id == "":
            print("ERROR: Enter a valid ID format (e.g. PXXX)")
            print("------------------")
            continue

        if "P" not in product_id or len(product_id) != 4:
            print("ERROR: Enter a valid ID format (e.g. PXXX)")
            print("------------------")
            continue

        break

    while True:
        product_name = input("Product Name: ")
        
        # Checks invalid inputs
        if product_name.isdigit() or product_name == "":
            print("ERROR: Enter a product name")
            print("------------------")
            continue
        break

    while True:
        price_amt = input("Price: ")

        try:
            price_float = float(price_amt)
            # Checks invalid inputs
            if price_float < 0:
                print("ERROR: Only positive numbers are allowed")
                print("------------------")
                continue

        # Checks if price is in 2 decimal places
            if "." in price_amt:
                decimal = price_amt.split(".")[1] 
                
                if len(decimal) > 2:
                    print("ERROR: Price cannot have more than 2 decimal places")
                    print("------------------")
                    continue
            break

        except:
            print("ERROR: Enter a valid price (2 decimal places)")

    while True:
        quantity_amt = input("Stock Quantity: ")

        # Checks invalid inputs
        if not quantity_amt.isdigit() or quantity_amt == "":
            print("ERROR: Enter a valid integer")
            print("------------------")
            continue

        if int(quantity_amt) < 0:
            print("ERROR: Only positive numbers are allowed")
            print("------------------")
            continue
        else:
            return Product(product_id, product_name, price_float, int(quantity_amt))

def update_stock():
    print("Update Stock")
    product_id_name = input("Enter Product ID/Name: ")
    product = orders.search_product(product_id_name)

    if product is None:
            print("Product not Found")
            return
    
    print("Name:", product.get_name())
    print("Current Stock:", product.get_quantity())

    new_quantity = input("\nNew Stock Quantity: ")
    product.update_stock(int(new_quantity))

    print("\nStock updated successfully!")

        
    print("Product ")

def search_product():
    print("Search Product")
    product_id_name = input("Enter Product ID/Name: ")
    product = orders.search_product(product_id_name)

    if product is None:
        print("Product not Found")
        return

    print("------------------------------------------------")
    print(f"ID: {product.get_id()}")
    print(f"Name: {product.get_name()}")
    print(f"Price: ${product.get_price():.2f}")
    print(f"Stock: {product.get_quantity()}")
    print("------------------------------------------------")

def save_inventory():
    inventory_file = "inventory.json"
    with open(inventory_file, "w") as json_file:
        json.dump(orders, json_file, indent=4)

# Load inventory file
def load_inventory():
    inventory_file = "inventory.json"
    # Sets the default starting ID

    # Checks for existence of "inventory.json"
    try:
        with open(inventory_file, "r") as file:
            print("\"inventory.json\" found.")
            print("\"inventory.json\" loaded successfully.")
            
            # Load json file
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("File not found")
        print("Creating \"inventory.json\"")

        with open(inventory_file, "w") as file:
            # Empty list saved to ensure created file is a valid JSON file
            json.dump([], file)
            print("\"inventory.json\" created.")

        

orders = Inventory()

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")
saved_data = load_inventory()

if saved_data:
    orders = saved_data

while True:
    option = menu_system()

    if option == 1:
        orders.display_all()

    if option == 2:
        product_details = add_product()
        orders.add_product(product_details)
        
        print("\nProduct added successfully!")

    if option == 3:
        update_stock()

    if option == 4:
        search_product()

    if option == 5:
        print("Saving inventory...")
        save_inventory()
        print("Inventory saved successfully to \"inventory.json\"")

    if option == 6:
        print("Saving inventory before exit...")
        save_inventory()
        print("Inventory saved successfully.\n")
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

