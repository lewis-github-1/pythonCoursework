######################################################
# NOTES:
# -	Look at the sampleoutput.png before starting the code
#	
# - The ONLY place you should be “hard-keying” a numeric value 
# 	is when you are assigning the tax rate to a variable.  
# 	Other than that, all expressions should consist only 
# 	variables, functions, or methods.
######################################################

# Step 1: Create an empty list named sale_items
sale_items = []


# Step 2: Ask ther user for 3 item prices and store the 
#		values in the sale_items list
item1 = float(input('Enter the price for item 1: '))
item2 = float(input('Enter the price for item 2: '))
item3 = float(input('Enter the price for item 3: '))
print()
sale_items.append(item1)
sale_items.append(item2)
sale_items.append(item3)

print(f"{'Price of item 1:':}{item1:12.2f}")
print(f"{'Price of item 2:':}{item2:12.2f}")
print(f"{'Price of item 3:':}{item3:12.2f}")
print()


# Step 3: Print the list 3 times:  
#		original order, reverse order, and sorted
print('Display item order variations:')
print('=================================')
print('Original:', sale_items)
sale_items.reverse()
print('Reversed:', sale_items)
sale_items.sort()
print('Sorted:  ', sale_items)
print()

# Step 4: Calculate the subtotal of the items 
#		and store result in a variable
subtotal = item1 + item2 + item3

# Step 5: Calculate the average price of the items 
#		and store result in a variable
average = subtotal / 3

# Step 6:  Calculate the tax on the subtotal using 
#		a tax rate of 9.25%
#		and store result in a variable
tax = subtotal * .0925

# Step 7: Calculate total of the order including tax
#		and store result in a variable
total = subtotal + tax

# Step 8: Neatly display the output like the sampleoutput.png
print('\nDisplay Receipt:')
print('=======================')
print(f'{"Item 1:":10}{item1:>10.2f}')
print(f'{"Item 2:":10}{item2:>10.2f}')
print(f'{"Item 3:":10}{item3:>10.2f}')
print('-----------------------')
print(f'{"Subtotal:":10}{subtotal:>10.2f}')
print(f'{"Tax:":10}{tax:>10.2f}')
print('=======================')
print(f'{"Total:":10}{total:>10.2f}')
print('-----------------------')
print(f'{"Average:":10}{average:>10.2f}')









