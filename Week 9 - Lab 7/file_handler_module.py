import json

from inventory_module import Inventory
from product_module import Product, PhysicalProduct, DigitalProduct

inventory_file = "inventory.json"

def save_inventory(inventory):

    add_data = []

    for product in inventory.get_inventory():
        add_data.append({
        "product_type": product.get_type(),
        "product_id": product.get_id(),
        "product_name": product.get_name(),
        "product_price": product.get_price(),
        "product_quantity": product.get_quantity(),
        "product_add_info": product.get_add_info()
        })

    with open(inventory_file, "w") as json_file:
        json.dump(add_data, json_file, indent=4)

# Load inventory file
def load_inventory(orders):

    # Checks for existence of "inventory.json"
    try:
        with open(inventory_file, "r") as file:
            print("\"inventory.json\" found.")
            print("\"inventory.json\" loaded successfully.")
            
            # Load json file
            data = json.load(file)

            # iterate through file, load each dictionary pairs
            for item in data:
                if item["product_type"] == "Physical":
                    product = PhysicalProduct(item["product_id"], item["product_name"], item["product_price"], item["product_quantity"], item["product_add_info"])
                    orders.add_product(product)

                elif item["product_type"] == "Digital":
                    product = DigitalProduct(item["product_id"], item["product_name"], item["product_price"], item["product_quantity"], item["product_add_info"])
                    orders.add_product(product)

        return data

    except FileNotFoundError:
        print("File not found")
        print("Creating \"inventory.json\"")

        with open(inventory_file, "w") as file:
            # Empty list saved to ensure created file is a valid JSON file
            json.dump([], file)
            print("\"inventory.json\" created.")