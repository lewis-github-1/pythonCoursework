def main():
	# replace pass with your code
  while True:
    try:
      hours = float(input("Please enter your hours: "))
      if hours < 0:
        print("Please enter a value greater than 0")
        continue
      else:
        break
    except:
      print("Please enter a numeric value greater than 0 ")
      
  print(), print()
       
  while True:
    try:
      rate = float(input("Please enter your rate: "))
      if rate < 8.25:
        print("Please enter a value greater than 8.25")
        continue
      else:
        break
    except:
        print("Please enter a numeric value greater than 8.25 ")

  print(), print()
  gross = hours * rate    # Gross pay calculation
  print("Hours:  ", f'{hours:>10.2f}')
  print("Rate:   ", f'{rate:>10.2f}')
  print("Gross:  ", "$", f'{gross:>8.2f}')
  

main()
   
# =====================================================================
# Instructions:  write the code that will:
# - 1) ask the user for their hours.  Hours must be a positive number
# - 2) ask the user for their pay rate.  Rate must be at least 8.25
# - 3) include code that will ask them for the values again 
# 		if they:
# 	- enter a string instead of a numeric value
# 	- enter a numeric value that is not within each range
# - 4) calcuate their gross pay and store it in a variable
# - 5) display their hours, rate, and gross pay nicely 
#			formatted in columns
#
# NOTES about validation:
# -------------------------------------------
# !!!! MAKE SURE YOU USE TRY / EXCEPT WHEN VALIDATING INPUT!!!!
# !!!! You should have separate try / excepts for 
#			 each type of validation:
#				- is the value numeric?
#				- is the value with the expected range?
#			 Don't try to make both into one try/except
# =====================================================================



