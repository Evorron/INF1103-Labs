# Imports
import json

from product_module import Product, PhysicalProduct, DigitalProduct
from inventory_module import Inventory
from file_handler_module import load_inventory, save_inventory

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
        # Checks for invalid product type
        product_type = input("Is this a Physical or Digital product? (P/D): ")
        if product_type.isdigit() or product_type == "":
            print("ERROR: Specify if it's a Physical or Digital product.")
            print("------------------")
            continue

        if product_type.lower() != "p" and product_type.lower() != "d":
            print("ERROR: Specify if it's a Physical or Digital product.")
            print("------------------")
            continue
        break

    while True:
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
        break

    while True:
        if product_type.lower() == "p":
            product_weight = float(input("Product Weight(kg): "))
            if product_weight <= 0 or product_weight == "":
                print("ERROR: Weight must be greater than 0")
                continue
            return PhysicalProduct(product_id, product_name, price_float, int(quantity_amt), product_weight)

        else:
            product_size = float(input("Product Download Size(Gb): "))
            if product_size <= 0 or product_size == "":
                            print("ERROR: Size must be greater than 0")
            return DigitalProduct(product_id, product_name, price_float, int(quantity_amt), product_size)
    

def update_stock():
    print("Update Stock")
    product_id_name = input("Enter Product ID/Name: ")
    product = orders.search_product(product_id_name)

    if product is None:
            print("Product not Found")
            return
    
    print("Name:", product.get_name())
    print("Current Stock:", product.get_quantity())

    while True:
        new_quantity = input("\nNew Stock Quantity: ")
        if new_quantity.isdigit() and int(new_quantity) >= 0: 
            product.update_stock(int(new_quantity))
            print("\nStock updated successfully!")
            break
        print("ERROR: Enter a valid non-negative integer")

        
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

# Instanitate Inventory object 
orders = Inventory()

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")
load_inventory(orders)

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
        save_inventory(orders)
        print("Inventory saved successfully to \"inventory.json\"")

    if option == 6:
        print("Saving inventory before exit...")
        save_inventory(orders)
        print("Inventory saved successfully.\n")
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

