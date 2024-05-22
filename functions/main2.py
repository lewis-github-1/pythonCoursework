def main():
  weight = get_number("Enter your weight in pounds: ")
  print()
  height = get_number("Enter your height in inches: ")
  print()
  bmi = calc_bmi(weight, height)
  determine_status(bmi)


def get_number(prompt):
	while True:
		number = int(input(prompt))
		if number <= 0:
			print("Please enter a positive value\n")
			continue
		else:
			return number


def calc_bmi(wt, ht):
  bmi = wt * 703 / (ht * ht)
  print(f"Your BMI is: {bmi:.2f}")
  return bmi

def determine_status(bmi):
  if bmi < 18.5:
    print("You are considered underweight.")
  elif bmi >= 18.5 and bmi <= 25:
    print("Your weight is optimal.")
  else:
    print("You are considered overweight.")
  return
  

  
main()




#def get_number(prompt):
#	while True:
#  	number = int(input(prompt))
#		if number <= 0:
#		  print("Please enter a positive value\n")
#			continue
#		else:
#			return number
