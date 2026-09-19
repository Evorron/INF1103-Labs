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


def process_delivery(current_total, new_value): # Delivery Calculation
    # 
    return

def calculate_tax(amount):
    return

def generate_report(total_units, failed_attempts):
    # Function takes in total inventory and failed/rejected attempts
    # Function returns the two values via print
    return


inventory = 0
failed_rejected = 0

while True:
    input_value = get_valid_input()

    # if 


    # else:
    #     inventory += int(count)
    #     print(inventory)

    #     if inventory > 500:
    #         print("Overstock alert")
    #         break
