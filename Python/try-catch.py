# If division  by zero happens, division by zero error occurs
# Else if invalid input , then invalid input error occurs

try:
    value = 10 / 0
    inp = float(input("Enter a float value "))
    print(inp)
except ZeroDivisionError:
    print("Division by zero error")

except ValueError:
    print("Invalid input error")
