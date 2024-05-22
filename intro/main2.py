# Step 1:	ask the user for their name and store it in a variable
user_name = input("Enter your name: ")

# Step 2:	ask the user for their hours and store the value in a variable
# 	Hint: remember that you will need to cast (change) this value to a float
#		so it can be used as a number
hours_worked = float(input("Enter your hours: "))

# Step 3:	ask the user for their rate and store the value in a variable
# 	Hint: remember that you will need to cast (change) this value to a float
#		so it can be used as a number
pay_rate = float(input("Enter your rate: "))


# Step 4:	calculate the pay by taking the hours multiplied by the rate 
#		and store the result in a variable
total_pay = hours_worked * pay_rate

# Step 5:  output the values, calling the variables where necessary
# 	see the sample output for what this should look lik
print("\n" + "Your name is ", user_name)
print("Hours: ", hours_worked)
print("Rate: ", pay_rate)
print("Pay: ", total_pay)




################################################################
# NOTES:
# 
# Remember good variable naming conventions:
# - meaningful name
# - all lower case letters with words separated by underscores
# 
# Make sure your code runs before submitting it!
################################################################