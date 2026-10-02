# Imports
import json

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
            return product_id, product_name, price_float, int(quantity_amt)

def update_stock():
    product_id_name = input("Enter Product ID/Name: ")
        
    for product_dict in orders:
        if product_dict["product_name"].lower() == product_id_name.lower() or product_dict["product_id"].lower() == product_id_name.lower():
            print("Product Found:")
            print("Name:", product_dict["product_name"])
            print("Current Stock:", product_dict["product_quantity"])

            new_quantity = input("\nNew Stock Quantity: ")
            product_dict["product_quantity"] = int(new_quantity)

            print("\nStock updated successfully!")

def search_product():
    product_id_name = input("Enter Product ID/Name: ")
    
    for product_dict in orders:
        if product_dict["product_name"].lower() == product_id_name.lower() or product_dict["product_id"].lower() == product_id_name.lower():
            print("Product Found")
            print("------------------------------------------------")
            print(f"ID: {product_dict["product_id"]}")
            print(f"Name: {product_dict["product_name"]}")
            print(f"Price: ${product_dict["product_price"]:.2f}")
            print("Stock:", product_dict["product_quantity"])
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
            file.seek(0)
            # Reads contents of inventory.txt
            current_inventory = file.read()

            for line in current_inventory.splitlines():
                # Checks the current order ID in inventory.txt
                order_id = int(line.split(",")[0])
                # Sets the next available ID for use
                highest_id = order_id + 1

                # Sums total inventory quantity
                total_quantity += int(line.split(",")[2])

        return current_inventory

    except FileNotFoundError:
        print("File not found")
        print("Creating \"inventory.json\"")

        with open(inventory_file, "a+") as file:
            print("\"inventory.json\" created.")

orders = []

load_inventory()

while True:
    option = menu_system()

    if option == 2:
        product_dict = {}
        product_details = add_product()
        pid, name, price, quantity = product_details

        product_dict["product_id"] = pid
        product_dict["product_name"] = name
        product_dict["product_price"] = price
        product_dict["product_quantity"] = quantity
        orders.append(product_dict)

        print("\nProduct added successfully!")

    if option == 3:
        update_stock()

    if option == 4:
        search_product()

    if option == 5:
        save_inventory()