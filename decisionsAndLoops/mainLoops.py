#========================================================
# Exercise #1 = while True
#========================================================
print("\nExercise 1:\n===================")
flag = True
while flag:
  print('The flag is', flag)
  flag = False

#========================================================
# Exercise #2 - nested if inside while
#========================================================
print("\nExercise 2:\n===================")
floor = 0
while floor < 15:
  floor += 1
  if floor == 13:
    print('No 13th floor')
  else:
    print('Floor', floor)
  
#========================================================
# Exercise #3 - counter controlled while loop
#========================================================
print("\nExercise 3:\n===================")
counter = 0

while counter <= 20:
  print(counter, end=' ')
  counter += 2
print()

#========================================================
# Exercise #4 - accumulator variable
#========================================================
print("\nExercise 4:\n===================")
total = 0
count = 0

while count <= 10:
  total += count
  count += 1

print('The total is', total)

#========================================================
# Exercise #5 - nested while
#========================================================
print("\nExercise 5:\n===================")
number = 1
pattern = '{:>3}'

print('''
Times Table:
===========================================''')

while number < 6:
  multiplier = 1
  while multiplier < 11:
    product = number * multiplier
    print(pattern.format(str(product)), end='')
    multiplier += 1
  print()
  number += 1
    
#========================================================
# Exercise #5 - input validation - number between 1 and 10
#========================================================
print("\nExercise 5:\n===================")
number = int(input('Enter a number between 1 and 10: '))

while number < 1 or number > 10:
  print('Invalid number')
  number = int(input('Enter a number between 1 and 10: '))

print('Your number is', number)

#========================================================
# Exercise #6 - input validation - use break and continue
#========================================================
print("\nExercise 6:\n===================")

while True: 
  number = int(input('Enter a number between 1 and 10: '))
  if number < 1 or number > 10:
    print('Invalid number')
    continue
  else:
    print('Your number is', number)
    break













