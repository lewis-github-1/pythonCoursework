# In this program, we are going to (roughly)
# calculate a person's age

# Task 1:  Put proper import statements here
from datetime import datetime, timedelta, date
import pytz

# Task 2:  Create a datetime object for the current date
date_now = datetime.now()
date_now_timezone = date_now.astimezone(pytz.timezone("US/Central"))

# Task 3:  Prompt the user to enter their birthdate in 
# whatever format you want to work with
birthdate = input("\nEnter your birthdate as mm-dd-yyyy: ")

# Task 4:  Convert the user input to a datetime object
datetime_birthdate = datetime.strptime(birthdate, "%m-%d-%Y")

# Task 5:  Create a variable called age that subtracts
# the birthdate variable from the current date/time variable
# BE SURE TO NAME THIS VARIABLE age SO THAT THE FORMULA IN STEP 6 WORKS
age = date_now - datetime_birthdate

# Task 6:  This step is already done.
# It calcuates the years by converting the age
# variable to the number of days and then divides by 365.2425
# YOU DO NOT NEED TO EDIT THIS FORMULA IF YOU USED age AS THE VARIABLE NAME
# IN STEP 5
years = age.days / 365.2425


# Task 7:  Output the results
# Refer to the sample output and try to match 
# your printout match as best you can
# Keep in mind that the sample output will be different
# since it ran on a different date
print("As of today", f"{date_now_timezone:%m-%d-%Y:}")
print("You are", int(years), "years old")
print("You were born on a", f"{datetime_birthdate:%A}")