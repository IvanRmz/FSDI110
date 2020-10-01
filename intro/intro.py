
def test():
    print("I'm a function")

def separator():
    print("----------------------")


separator()
print("Hello Python")

separator()

# Variables
name = "Ivan"
last = "Ramirez"
age = 28
found = False
total = 23.43
products = []

print(name)
print(name + " " + last)

print (name + str(age))

separator()

# math operation

print(age - 10)
print(age + 10)
print(age * 2)
print(age / 2)
print(age % 2)

separator()

# if statements

if (age < 80):
    print("You are still young!")
    print("Something else")
elif (age == 80):
    print("You are on the border line")
else:
    print("Sorry, you are getting old :|")