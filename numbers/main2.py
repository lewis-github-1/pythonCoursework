# Instructions:
#----------------------------------------------------------------
# Task 1:  Ask the user for 3 values and store in 3 different variables
# Task 2:  Make sure the values are converted to floating point numbers
# Task 3:  Calculate the subtotal (all 3 items added together)
# Task 4:  Calculate the sales tax (subtotal multiplied by .0925)
# Task 5:  Calculate the total (subtotal added to the tax amount)
# Task 6:  Display the values using formatting and columns. (see sample)

value_one = float(input("Enter the price for item one: "))
value_two = float(input("Enter the price for item two: "))
value_three = float(input("Enter the price for item three: "))
print()
subtotal = value_one + value_two + value_three
sales_tax = subtotal * .0925
total = subtotal + sales_tax

print("Sales Receipt:")
print("======================")
print(f"{'Item 1:':10} {value_one :10.2f}")
print(f"{'Item 2:':10} {value_two :10.2f}")
print(f"{'Item 3:':10} {value_three :10.2f}")
print("======================")
print(f"{'Subtotal:':10} {subtotal :10.2f}")
print(f"{'Sales Tax:':10} {sales_tax :10.2f}")
print(f"{'Total:':10} {total :10.2f}")

























