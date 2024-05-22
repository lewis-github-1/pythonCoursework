class Person:
  def __init__(self, fname, lname):
    self.first_name = fname
    self.last_name = lname
  
  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.grad_year = year

  def __str__(self):
    return super().__str__() + " graduation year: " + str(self.grad_year)

class Grad_Student(Student):
  def __init__(self, fname, lname, year, credential):
    super().__init__(fname, lname, year)
    self.credential = credential

  def __str__(self):
    return super().__str__() + " credential: " + self.credential


def main():
  p1 = Person("Jane", "Doe")
  print(p1)
  print(type(p1))
  print()
  
  s1 = Student("John", "Doe", 2024)
  print(s1)
  print(type(s1))
  print()

  g1 = Grad_Student("Billy", "Joel", 2025, "Masters")
  print(g1)
  print(type(g1))
  print()

  people = [p1, s1, g1]
  
  for p in people:
    print()
    print(p)
    print(type(p))
    print("Person?", isinstance(p, Person))
    print("Student? ", isinstance(p, Student))
    print("Grad Student? ", isinstance(p, Grad_Student))

main()