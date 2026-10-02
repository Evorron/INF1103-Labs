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
   
   return int(option)
    

def add_product():
# Prompts and retrieves user input
    while True:
        print("\nAdd New Product")
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
            return product_name, float(price_amt), int(quantity_amt)

# Load inventory file
def load_inventory():
    inventory_file = "inventory.json"
    # Sets the default starting ID
    highest_id = 1001
    total_quantity = 0

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

        return current_inventory, highest_id, total_quantity

    except FileNotFoundError:
        print("File not found")
        print("Creating \"inventory.json\"")

        with open(inventory_file, "a+") as file:
            print("\"inventory.json\" created.")

        return highest_id, total_quantity

orders = []

load_inventory()

while True:
    option = menu_system()

    if option == 2:
        product_dict = {}
        product_details = add_product()
        name, price, quantity = product_details

        product_dict["product_name"] = name
        product_dict["product_price"] = price
        product_dict["product_quantity"] = quantity
        orders.append(product_dict)

    break

print(orders)