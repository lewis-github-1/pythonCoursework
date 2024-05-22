user_name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(user_name)
print(age)

print(user_name + " is " + str(age) + " years old ")

pay_rate = float(input("Enter your rate: "))
print("You make $", pay_rate, "per hour")
print("A 10% raise would give you $", round(pay_rate * 1.1, 2))