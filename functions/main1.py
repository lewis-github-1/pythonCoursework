def get_double(prompt):
  while True:
    number = float(input(prompt))
    if number <= 0:
      print("Please enter a positive value")
      continue
    else:
      return number

def calc_gross(hours, rate):
  return hours * rate

def calc_net(gross):
  fed = gross * .2
  state = gross * .0495
  fica = gross * .0725
  net = gross - fed - state - fica
  return net

def main():
  rate = get_double('Enter the rate of pay: ')
  hours = get_double('Enter your hours worked: ')
  gross = calc_gross(hours, rate)
  net = calc_net(gross)
  pattern = "{:<8}${:>8.2f}"
  print("\nPay Calculations:\n=====================")
  print(pattern.format("Gross:", gross))
  print(pattern.format("Net", net))

main()




