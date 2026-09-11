inventory = 0
failed_rejected = 0

while True:
    count = input("Enter stock quantity: ")
    # Exit condition
    if count == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries: ", failed_rejected)
        break