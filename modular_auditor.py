# Functions
def get_valid_input(): # Input prompt and Validation
    # Prompts and retrieves user input
    user_input = input("Enter stock quantity: ")

    # Exit condition
    if user_input.lower() == "quit":
        return user_input.lower()
    
    # Checks invalid inputs
    if not user_input.isdigit() or user_input == "":
        print("ERROR: Enter a valid integer")
        return None

    if int(user_input) < 0:
        print("ERROR: Only positive numbers are allowed")
        return None

    else:
        return int(user_input)

def process_delivery(current_total, new_value): # Delivery amount calculation
    return current_total + new_value

def calculate_tax(amount):
    return

def generate_report(total_units, failed_attempts):
    print("\n-------Final Summary-------")
    print("Total Delivery Processed:", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)


total_inventory = 0
failed_rejected = 0
deliveries_processed = 0

while True:
    input_value = get_valid_input()

    if input_value == "quit":
        generate_report(total_inventory, failed_rejected)
        break

    if input_value == None:
        failed_rejected += 1
        continue

    # Adds delivery amount to total inventory
    total_inventory = process_delivery(total_inventory, input_value)

    deliveries_processed += 1

    if total_inventory > 500:
            print("OVERSTOCK ALERT")
            break