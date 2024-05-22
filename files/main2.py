import random

def main():
	# Open a file to write to named numbers.txt
  file_one = open('numbers.txt', 'w')
	# Write 50 random numbers between 1 and 100 to the file
  for i in range(50):
    number = random.randrange(1, 100)
    file_one.write(str(number) + "\n")
      
	# Close the file
  file_one.close()
	# Open the numbers.txt file again for reading
  file_one = open('numbers.txt', 'r')
	# Create an empty list named numbers
  numbers = []
	# Read the numbers from the file into a list
  for line in file_one:
    line = line.replace("\n", "") #removes new line
    numbers.append(int(line))
  print('The list is: \n')
  print(numbers)
  print()
  # Close the file
  file_one.close()
	# Print how many elements in the list using a list method
  length = len(numbers)
  print('There are', length , 'numbers in the list')
	# Print the total of the list using a list method
  total = sum(numbers)
  print('The total is',total)
	# Print the average of the numbers in the list using list methods
  average = sum(numbers) / len(numbers)
  print('The average is', average)
  print()
	# Print the highest value using the max method for a list
  maximum = max(numbers)
  print('The highest number is', maximum)
	# Print how many times your highest value appears in the list
  highest_count = numbers.count(maximum)
  print('It appears', highest_count, 'time(s)')
  print()
	# Print the lowest value using the min method for a list
  minimum = min(numbers)
  print('The smallest number is', minimum)
	# Print how many times the lowest value appears in the list
  lowest_count = numbers.count(minimum)
  print('It appears', lowest_count, 'time(s)')




main()