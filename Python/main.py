from math import *

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

# Variables , Strings and bool
name = "Ranjan"
isTrue = True
print("My name is " + name + " for " + str(isTrue))
# or
print("My name is", name, "for", isTrue)
# using commas instead of plus has adavantage.. It automatically recognises the space between words.
# But while using + , we have to provide spaces if we require
print(name.upper())
print(name[0])
print(name.replace("Ranjan", "Ranjan R Upadhya"))

# Numbers and math functions (inbuilt)
Number = -100
print(abs(Number))
print(pow(Number, 2))

# math functions from imported math lib
print("Ceil of 0.95 is", ceil(0.95))
print("Floor of 0.95 is", floor(0.95))

# getting input from user
name = input("Enter your name ")
age = int(input("Enter your age "))
print("Hello", name, "and you are", age, "years old")
