# Menu
def menu_system():
   print("----------- MENU -----------")
   print("1. Display All Products")
   print("2. Add Product")
   print("3. Update Stock")
   print("4. Search Product")
   print("5. Save Inventory")
   print("6. Exit")
   print("-----------------------------\n")

   option = input("Enter option: ")

   if option.isdigit():
       if option == 1:
           pass
       if option == 2:
           pass
       if option == 3:
           pass
       if option == 4:
           pass
       if option == 5:
           pass
       if option == 6:
           pass

# Load inventory file
def load_inventory():
    # Sets the default starting ID
    highest_id = 1001
    total_quantity = 0

    # Checks for existence of "inventory.json"
    try:
        with open("inventory.json", "a+") as file:
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

    except FileNotFoundError:
        print("File not found")
        print("Creating \"inventory.json\"")

        with open("inventory.json", "a+") as file:
            print("\"inventory.json\" created.")
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