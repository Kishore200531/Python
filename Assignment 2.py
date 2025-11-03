#Task 1: Check if a Number is Even or Odd
print("Task 1")

#Taking input from the user
num = int(input("Enter a number: "))

#Checking the number is even or odd using if-else statement
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")



#Task 2: Sum of Integers from 1 to 50
print("Task 2")
sum = 0
for i in range(1,51):
    sum += i

print("The sum of numbers from 1 to 50 is:", sum)
