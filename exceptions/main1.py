def main():
  import random
  computer = random.randint(1,50)
  print(computer)

  num_guesses = 5
  correct = False

  while not correct and num_guesses > 0:
    print()
    print("You have", num_guesses, "guesses remaining")
    try:
      user = int(input("Enter a number between 1 and 50: "))
      if user == computer:
        print()
        print("You win!!!")
        correct = True
      elif user < computer:
        print("Too low!")
      else:
        print("Too high!")
      num_guesses -= 1
      if num_guesses == 0 and not correct:
        print("You are out of guesses")
    except:  
      print("Invalid entry - try again.")
      continue
main()