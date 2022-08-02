# Task - Create a string variable called my_string and assign it a string that has at least 10 characters. Then ask user to enter a start index and end index and print the substring from the start index to the end index. ask user for the step size.

my_string = "Hello World"

print("Length of the string is", len(my_string))
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))

print(my_string[start_index:end_index])

step = int(input("Enter step size: "))

print(my_string[start_index:end_index:step])