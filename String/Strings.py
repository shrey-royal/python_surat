'''
What are strings?
Strings are sequences of characters.

J
I
G
A
R

Jigar - string



'''


# 1. Create a string variable called my_name and assign it your name.

# my_name = "Jigar"

# print(my_name)
# print(type(my_name))

# # index of string starts with 0
# # to access a character in a string use index
# print(my_name[2])

# print(my_name[4])

# # 2. Create a string variable called my_age and assign it your age.

# my_age = "21"

# print(type(my_age))


#################################################

# Slicing of strings - A string will be sliced from the start index to the end index.


my_string = "Hello, My name is Jigar"

print(len(my_string))   # length of string

# Slice - my_string[start_index:end_index]

# my_string_slice = my_string[0:5]

# end_index - 1

# print(my_string_slice)

# print(my_string[0:len(my_string)])


# my_string = "Hello, My name is Jigar"
# My name is Jigar

# print(my_string[7:23])
# print(my_string[18:23])

# print(my_string[7:])
# print(my_string[:7])

# till here we did slicing of strings using positive indexing

# Negative indexing - starts from the end of the string
'''
0   1   2   3   4
H   E   L   L   O
-5  -4  -3  -2  -1

'''
new_string = "Hello"

# print(new_string[-5:])
# print(new_string[-4:])


# step -> step size

# slicing -> start_index:end_index:step_size

# step size means how many characters we want to skip

#positive indexing

# step size - 1 
# H  E   L   L   O
print(new_string[::2])

# negative indexing

print(new_string[::-1])


# Task - Create a string variable called my_string and assign it a string that has at least 10 characters. Then ask user to enter a start index and end index and print the substring from the start index to the end index. ask user from the step size.