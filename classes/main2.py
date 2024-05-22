class Patient:
	# create __init__() method=====================
  def __init__(self, nm, wt, ht):
    self.name = nm
    self.weight = wt
    self.height = ht

	# calculate and return BMI=====================
  def getBMI(self):
    return self.weight / pow(self.height,2) * 703

	# decide BMI category==========================
  def getStatus(self):
    if self.getBMI() > 25:
      return "obese"
    elif self.getBMI() < 18.5:
      return "underweight"
    else:
      return "optimal"

	# custom string output method================
  def __str__(self):
    message = f"Name:\t{self.name}"
    message += f"\nWeight:\t{self.weight}"
    message += f"\nHeight:\t{self.height}"
    message += f"\nBMI:\t{self.getBMI():.2f}"
    message += f"\nStatus:\t{self.getStatus()}"
    return message
		
def main():
	# create instance with literals======================
  p1 = Patient("Tom Sawyer", 175, 65)
  print("\nPrinting instance made with literal values....")
  print("==============================================")
  print(p1)

	# accessing class method directly====================
  print("\nAccessing BMI calculation directly....")
  print("============================================")
  print(f"The BMI is {p1.getBMI():.2f}")

	# create instance from user input====================
  print("\nGetting user input....")
  print("=========================================")
  input_name = input("Enter your name: ")
  input_weight = int(input("Enter your weight in pounds: "))
  input_height = int(input("Enter your height in inches: "))
  p2 = Patient(input_name, input_weight, input_height)

  print()
  print("\nPrinting instance made with user supplied values....")
  print("===================================================")
  print(p2)


main()