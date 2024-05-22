hours = float(input("Enter your hours: "))
rate = float(input("Enter your rate: "))

if hours > 40:
  ot_hours = hours - 40
  ot_pay = ot_hours * 1.5 * rate
  base_pay = 40 * rate
  gross = ot_pay + base_pay
else:
  gross = hours * rate

federal = gross * .15
state = gross * .0495
fica = gross * .0725
net = gross - federal - state - fica

print()
print("Pay Calculations:")
print("======================")
print(f"{'Hours':10}{hours:11.2f}")
print(f"{'Rate':10}${rate:10.2f}")
print("----------------------")

print(f"{'Gross':10}${gross:10.2f}")
print(f"{'Federal':10}${federal:10.2f}")
print(f"{'State':10}${state:10.2f}")
print(f"{'FICA':10}${fica:10.2f}")
print("----------------------")
print(f"{'Net':10}${net:10.2f}")

print()
if hours > 40:
  print(f"**Includes${ot_pay:.2f} of overtime pay")


















