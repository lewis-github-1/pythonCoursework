class Animal:
  def __init__(self, nm, tp):
    self.name = nm
    self.type = tp

  def __str__(self):
    return self.name + " is a(n) " + self.type


class Dog(Animal):
  def __init__(self, nm, tricks):
    super().__init__(nm, "dog")
    self.tricks = tricks

  def __str__(self):
    temp = super().__str__()
    temp += "\nTricks: " + self.tricks
    return temp


class Cat(Animal):
  def __init__(self, nm, personality):
    super().__init__(nm, "cat")
    self.personality = personality

  def __str__(self):
    temp = super().__str__()
    temp += "\nPersonality: " + self.personality
    return temp


def main():
  a1 = Animal("Roger", "rabbit")
  print(a1)
  print(type(a1))
  print(isinstance(a1, Animal))
  print()

  d1 = Dog("Fido", "fetches")
  print(d1)
  print(type(d1))
  print(isinstance(d1,Animal))
  print(isinstance(d1,Dog))
  print()


  c1 = Cat("Morris", "sassy")
  print(c1)
  print(type(c1))
  print(isinstance(c1,Animal))
  print(isinstance(c1,Cat))
  print(isinstance(c1,Dog))
  print()


  animals = [a1, d1, c1]

  for animal in animals:
    print()
    print(animal)
    print(type(animal))
    print(isinstance(animal, Animal))

main()