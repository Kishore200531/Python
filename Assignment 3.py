#Task 1: Factorial of a number using function
print("Task 1")
print()

#defining function
def factorial(number):
    if number == 0:
        return 1
    else:
        fact = number * factorial(number - 1)
        return fact

num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is: {result}")


print("============================")
#Task 2: Using the math module for calculations
print("Task 2")
print()

import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
log_e = math.log(num)
sine = math.sin(num)

print(f"Square root: {square_root}")
print(f"Logarithm: {log_e}")
print(f"Sine: {sine}")
