# Task 1) use a while loop to ask the user for 
#    a number between 1 and 10
#    Ask the user to re-enter if the number is not 
#    between 1 and 10:
number = int(input("Enter a number between 1 and 10: "))
while number < 1 or number > 10:
  print("Invalid entry, please re-enter")
  print()
  number = int(input("Enter a number between 1 and 10: "))
    

# Task 2) use a for loop to display the first 10
#    multiple of the user's number
print()
print("The first 10 multiples of your number are: ")
print("==========================================")
for i in range(1, 11):
  print(number * i, end=" ")


# Task 3) use the loop of your choice to 
#    add up the numbers up to and including the 
#    user's number.  For example, if the user
#    chosee 5, you would add 1+2+3+4+5 and would get 15 
#    HINT: you will need an accumulator variabl that is 
#    set to 0 to add the numbers to
print()
print()
counter = 0
total_counter = 0
while counter < number:
  counter += 1
  total_counter += counter
else:
  
# Task 4) Display the results of Task 3
  
  print("The total of the numbers 1 thru the number you entered is:", total_counter)





























