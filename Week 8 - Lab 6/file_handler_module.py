import json

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