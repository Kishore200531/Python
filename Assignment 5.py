#Task 1: Create a Dictionary of Student Marks
print("Task 1")

student_details = {'Alice': 85, 'Carol': 89, 'Moses': 92.5}

user_input = input("Enter thr student's name: ")

if user_input in student_details:
    print(f"{user_input}'s marks: {student_details[user_input]}")
else:
    print("Student not found.")

print("================================")

#Task 2: Demonstrate List Slicing
print("Task 2")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:",nums)

#Extracting first five elements
first_five = nums[:5:1]

#Reversing the extracted elements
reverse_list = first_five[::-1]
#extract_list = first_five.copy()
#extract_list.reverse()

#Printing both the lists
print("Extracted first five elements:",first_five)
print("Reversed extracted elements:",reverse_list)
