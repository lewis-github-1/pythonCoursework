# create an empty list
scores = []

print("\nGetting the values:\n=========================")
# ask for the first score and add it to the list
score1 = int(input('Enter the first score:\t'))
scores.append(score1)

# ask for the second score and add it to the list
score2 = int(input('Enter the second score:\t'))
scores.append(score2)

# ask for the third score and add it to the list
score3 = int(input('Enter the third score:\t'))
scores.append(score3)

# print the scores in actual order, then reversed, then sorted:
print("\nList order variations:\n=========================")
print("Original:\t", scores)
scores.reverse()
print("Reversed:\t", scores)
scores.sort()
print("Sorted:\t\t", scores)

# find the score statistics
total = sum(scores)
count_scores = len(scores)
average = total / count_scores
lowest = min(scores)
highest = max(scores)

# use a for loop to display each score on its own line
print("\nUsing a for loop:\n=========================")
for score in scores:
  print("Score:", score)

# output the statistics results
print('\n\nStatistics for the scores:')
print('============================')
print(f'{"Total":15}{total:>8d}')
print(f'{"Count":15}{count_scores:>8d}')
print(f'{"Highest":15}{highest:>8d}')
print(f'{"Lowest":15}{lowest:>8d}')
print(f'{"Average":15}{average:>8.2f}')

# use list comprehension to raise each score by 2%
print("\nUsing list comprehension:\n=========================")
new_scores = [n * 1.02 for n in scores]
print(new_scores)
