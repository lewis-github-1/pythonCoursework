# Instructions:
# - Ask the user for the hours
# - Ask the user for the rate
# - Calculate the following and store in variables:
# 		gross ( hours x rate)
#			federal withholding (gross x 15%)
# 		statewithholding (gross x 4.95%)
# 		fica withholding (gross x 7.25%)
# 		net (gross - federal - state - fica)
# - Use f-strings to output the data similar
#			to the sampleoutput.png

hours = float(input("Enter your hours: "))
rate = float(input("Enter your rate: "))

gross = hours * rate
federal = gross * .15
state = gross * .0495
fica = gross * .0725
net = gross - federal - state - fica

print()
print("Pay Calculations:")
print("======================")
print(f"{'Hours:':10} {hours:10.2f}")
print(f"{'Rate:':10} {rate:10.2f}")
print("----------------------")
print(f"{'Gross:':10} {gross:10.2f}")
print(f"{'Federal:':10} {federal:10.2f}")
print(f"{'State:':10} {state:10.2f}")
print(f"{'FICA:':10} {fica:10.2f}")
print("======================")
print(f"{'Net:':10} {net:10.2f}")





