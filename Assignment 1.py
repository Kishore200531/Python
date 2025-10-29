#Task 1: Perform Basic Mathematical Operations
print("Task 1")

#Taking two numbers as input from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

#Performing the basic mathematical operations
add = a + b
sub = a - b
mul = a * b
div = a / b

#Displaying the results of each operation
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
#print("Addition: {0}, Subtraction: {1}, Multiplication: {2}, Division: {3}".format(add, sub, mul, div))



#Task 2: Create a Personalized Greeting
print("Task 2")

#Taking user's first name and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

#Concatenating the first name & last name into a full name
full_name = first_name + " " + last_name

#Printing a Personalized greeting message
print("Hello, ", full_name, "! Welcome to the Python program.", sep="")
#print("Hello, {0}! Welcome to the Python program.".format(full_name))
