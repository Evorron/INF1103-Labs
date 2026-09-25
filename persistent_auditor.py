# ------Functions------
# Input prompt and Validation
def get_valid_input():
    # Prompts and retrieves user input
    user_input = input("Enter stock quantity: ")
    print("------------------")

    # Exit condition
    if user_input.lower() == "quit":
        return user_input.lower()
    
    # Checks invalid inputs
    if not user_input.isdigit() or user_input == "":
        print("ERROR: Enter a valid integer")
        print("------------------")
        return None

    if int(user_input) < 0:
        print("ERROR: Only positive numbers are allowed")
        print("------------------")
        return None

    else:
        return int(user_input)

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
    # Opens inventory.txt file if it exists, else creates it
    with open("inventory.txt", "r") as file:
        file.seek(0)
        current_inventory = file.read()
    return current_inventory

# Saves inventory
def save_inventory():
    # Each product entered stored onto a list
    # List format [ID, Product Name, Quantity]
    # Repeat items should be added to the same list
    # Upon saving, all list items saved into inventory.txt
    pass

total_inventory = 0
failed_rejected = 0
deliveries_processed = 0

while True:
    load_inventory()
    input_value = get_valid_input()

    if input_value == "quit":
        generate_report(total_inventory, failed_rejected)
        break

    if input_value == None:
        failed_rejected += 1
        continue

    if total_inventory > 500:
        print("OVERSTOCK ALERT")
        break

    # Adds delivery amount to total inventory
    total_inventory = process_delivery(total_inventory, input_value)
    tax = calculate_tax(input_value)
    deliveries_processed += 1

    delivery_details(input_value, tax, total_inventory, deliveries_processed)
