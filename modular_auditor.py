# Functions
def get_valid_input(): # Input Validation
    # Prompts and retrieves user input
    # Check input for "quit" -> Returns "quit" signal if True
    # Checks if user input is a valid integer -> Returns the integer value if True
    return

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
    count = input("Enter stock quantity: ")
    # Exit condition
    if count == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries: ", failed_rejected)
        break

    elif count.isdigit() != True or inventory < 0 or count == "":
            failed_rejected += 1
            print("Error")
            continue

    else:
        inventory += int(count)
        print(inventory)

        if inventory > 500:
            print("Overstock alert")
            break
