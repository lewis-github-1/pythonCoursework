# Task 1) create a dictionary to hold the following witholding rates:
# federal	.20
# state		.0495
# fica		.0725

rate_dictionary = {'Federal': .20, 'State': .0495, 'FICA': .0725}

# The following function has already been written for you.
# It takes 3 parameters: the minimum, the maximum, 
# 		and the input prompt
# It checks for a valid value - if not valid, it 
# 		asks the user again.  If it is valid, it returns the value
def get_valid_number(min, max, prompt):
	while True:
		user_number = float(input(prompt))
		if user_number < min or user_number > max:
			print('Invalid entry.  Please re-enter.')
			continue
		else:
			return user_number

# NOTE:  all the rest of the tasks will be written
# 		in the main() function below.  Pay attention to indentation
# 		Put the code beneath the corresponding comment/task
def main():
	# Task 2) use a for loop to display all the keys and values
  print('\nWithholding rates are:\n======================')
  for user_number in rate_dictionary:
    print(f'{user_number:8s}', f'{rate_dictionary[user_number]:8.2f}')
	
	# Task 3) call the get_valid_number() function 
	# 		to ask for the rate.
	# 		Valid values:  between 8.25 and 20.00
  rate = get_valid_number(8.25, 20.00, "\nEnter your pay rate: ")
	
	# Task 4) call the get_valid_number() funtion 
	# 		to ask for the hours.
	# 		Valid values:  between 0 and 40
  hours = get_valid_number(0, 40, "\nEnter your hours: ")
	
	# Task 5) calculate and store the gross pay (hours x rate)
  gross_pay = rate * hours
  
	# Task 6) calculate and store the federal witholding
	# 		Be sure to use the appropriate value from the dictionary
  federal_tax = gross_pay * (rate_dictionary['Federal'])
  
	# Task 7) calculate and store the state witholding
	# 		Be sure to use the appropriate value from the dictionary
  state_tax = gross_pay * (rate_dictionary['State'])
  
	# Task 8) calculate and store the fica witholding
	#		Be sure to use the appropriate value from the dictionary
  fica_tax = gross_pay * (rate_dictionary['FICA'])
  
	# Task 9) calculate and store the net amount 
	# 		(gross - federal - state - fica)
  net_amount = gross_pay - federal_tax - state_tax - fica_tax
  
	# Task 10) print out the results
  print("\nPaycheck info:")
  print("-------------------------")
  print("Gross ", f'{gross_pay:12.2f}')
  print("Federal ", f'{federal_tax:10.2f}')
  print("State ", f'{state_tax:12.2f}')
  print("FICA ", f'{fica_tax:13.2f}')
  print("=========================")
  print("Net ", f'{net_amount:14.2f}')


main()