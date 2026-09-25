# ------Functions------
# Input prompt and Validation
def get_valid_input():
    # Prompts and retrieves user input
    while True:
        product_input = input("Enter Product Name: ")
        
        # Exit condition
        if product_input.lower() == "quit":
            return product_input.lower()
        
        # Checks invalid inputs
        if product_input.isdigit() or product_input == "":
            print("ERROR: Enter a product name")
            print("------------------")
            return None

        break

    while True:
        quantity_input = input("Enter Quantity: ")

        # Checks invalid inputs
        if not quantity_input.isdigit() or quantity_input == "":
            print("ERROR: Enter a valid integer")
            print("------------------")
            return None

        if int(quantity_input) < 0:
            print("ERROR: Only positive numbers are allowed")
            print("------------------")
            return None

        else:
            return product_input, int(quantity_input)

# Delivery amount calculation
def process_delivery(current_total, new_value): 
    return current_total + new_value

# Calculates tax for the current delivery amount
def calculate_tax(amount):
    return amount * 0.10

# Display's current delivery information (NOT LAB SPECIFC FUNCTION)
def delivery_details(delivery_amount, tax_amount, current_total, current_processed): 
    print("Delivery Amount: ", delivery_amount)
    print("Tax: ", tax_amount)
    print("Current Inventory: ", current_total)
    print("Deliveries Processed: ", current_processed)
    print("------------------")

# Displays final summary
def generate_report(total_units, failed_attempts):
    print("\n-------Final Summary-------")
    print("Total Delivery Processed:", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

# Load inventory file
def load_inventory():
    # Sets the default starting ID
    highest_id = 1001
    total_quantity = 0
    with open("inventory.txt", "a+") as file:
        file.seek(0)
        # Reads contents of inventory.txt
        current_inventory = file.read()

        for line in current_inventory.splitlines():
            # Checks the current order ID in inventory.txt
            order_id = int(line.split(",")[0])

            # Sums total inventory quantity
            total_inventory += int(line.split(",")[2])

            # Sets the next available ID for use
            if order_id > highest_id:
                highest_id = order_id + 1

       

    return current_inventory, highest_id, total_quantity

# Saves inventory
def save_inventory(orders):
    # Each quantity entered stored onto a list
    with open("inventory.txt", "a") as file:
        for order in orders:
                file.write(f"{order[0]}, {order[1]}, {order[2]}\n")

orders = []
current_inventory, order_id, total_quantity = load_inventory() # Unpack load_inventory()
failed_rejected = 0
deliveries_processed = 0

print(f"Current Orders: \n\n\n{current_inventory}\n")

while True:
    user_input = get_valid_input()

    if user_input == "quit":
        print("Order successfully saved to inventory.txt")
        save_inventory(orders)
        generate_report(total_quantity , failed_rejected)
        break

    if user_input == None:
        failed_rejected += 1
        continue

    if total_quantity > 500:
        print("OVERSTOCK ALERT")
        break

    product, quantity = user_input
    orders.append([order_id, product, quantity])
    print(f"\nNew Order Added:\n{order_id}, {product}, {quantity}\n")
    order_id += 1

    # Adds delivery amount to total inventory
    # total_inventory = process_delivery(total_inventory, quantity)
    # tax = calculate_tax(input_value)
    deliveries_processed += 1

    # delivery_details(input_value, tax, total_inventory, deliveries_processed)
