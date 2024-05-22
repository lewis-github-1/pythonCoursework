class Employee:
  def __init__(self, fname, lname):
    self.first_name = fname
    self.last_name = lname

  def get_pay(self):
    return 0

  def __str__(self):
    return f"Employee: {self.first_name} {self.last_name}"

  
    
class CommissionEmployee(Employee):
  def __init__(self, fname, lname, sales, rate):
    super().__init__(fname, lname)
    self.sales = sales
    self.rate = rate

  def getpay(self):
    return f"{self.sales * self.rate:.2f}"

  def __str__(self):
    temp = super().__str__()
    temp += " is commissioned and earned " + str(self.getpay())
    return temp
   
  
    
class HourlyEmployee(Employee):
  def __init__(self, fname, lname, hours, rate):
    super().__init__(fname, lname)
    self.hours = hours
    self.rate = rate

  def getpay(self):
    return f"{self.hours * self.rate:.2f}"

  def __str__(self):
    temp = super().__str__()
    temp += " is hourly and earned " + str(self.hours * self.rate)
    return temp


def main():
  e1 = Employee("John", "Doe")
  
  c1 = CommissionEmployee("Jane", "Doe", 5000, .06)
  
  h1 = HourlyEmployee("Darth", "Vader", 35, 10.25)
  
  emp_list = [e1, c1, h1]
  for emp in emp_list:
    print(emp)
    print(type(emp))
    print("Employee? ", isinstance(emp, Employee))
    print("Commissioned employee? ", isinstance(emp, CommissionEmployee))
    print("Hourly employee? ", isinstance(emp, HourlyEmployee))
    print()


main()