#Task 1: Read a File and Handle errors
print("Task 1")
print()

#Creating a file
var = open("sample.txt", 'wt')
var.write("This is a sample text file.")
var.write("\nIt contains multiple lines.")
var.close()

#Reading the content in the file
try:
    var = open("sample.txt", 'rt')
    print("Reading file content:")
    data1 = var.readline()
    data1 = data1.strip()
    print("Line 1: ", data1)
    data2 = var.readline()
    data2 = data2.strip()
    print("Line 2: ", data2)

#Handling the errors
except FileNotFoundError:
    print("Error: The file sample.txt was not found.")

finally:
    var.close()


print("====================================")

#Task 2: Write and Append Data to a file
print("Task 2")
print()

user_input = int(input("Enter 25: "))
print()

if user_input == 25:
    data = "Hello, Python!"
    print(f"Enter text to write to the file: {data}")
    #Writing data into a file
    var = open("output.txt", 'wt')
    var.write(data)
    print("Data successfully written to output.txt.")
    var.close()

    print()
    #Appending data into a file
    var = open("output.txt", 'at')
    add_data = "Learning file handling in Python."
    print(f"Enter additional text to append: {add_data}")

    var.write("\n") #For next line
    var.write(add_data)
    print("Data successfully appended.")
    var.close()

    print()
    #Printing the content in the file
    var = open("output.txt", 'rt')
    print("Final content of output.txt:")
    print(var.read())
    var.close()

else:
    print("Enter 25 to continue.")
