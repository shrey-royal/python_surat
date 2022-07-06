'''

# print the data on the terminal
# how to scan the data form the user

# print("Hello")

# i want to create a program that scans 2 number form the user and just print them

# number stores in a variable

# What is a variable?
# a name of any memory location (RAM)

# you have to take sensible names

# addition -> total, sum, etc.

# variable_name = value


number = 1234 # variable

print(number) # we are printing the variable

# if we want to scan in python, we will use a method that called input().

# arguments -> ""

number_1 = float(input("Enter any float: "))
number_2 = int(input("Enter any integer: "))
name = input("Enter any string: ")

print(number_1, number_2, name, sep=",\t")

print(type(number_1), type(number_2), type(name), sep=", \t")
'''



'''

input function-: 

> this function is used to scna data from the user.
> the default data type of this input function is string (str).
> we can convert the data into any datatype by using this method -> int(input())

Datatypes-:

variable-: it stores the values...

Data types defines that what type of data will be stored in any variable.

# int -> integer -> 12, 1, 2, 3, 54, 435, etc.
# float -> floating values -> 2.3, 4.5, etc.
# char -> character -> a, b, e, s, etc.
# str -> string -> name, jigar, 124, 2.4, a, w, etc.

in python we don't have the char data type

any datatype can be converted into string



Task -: 

# you have ask the user for his/her firstname, middlename, lastname an then print them


# Operators-: Operators are the functions that takes input, process that input and give us back the output.

types of operators-: 

1. Arithmetic Operator-: 

Addition -> +
subtraction -> -
multiplication -> *
division -> / -> 5.0
floor division -> // -> roundof -> 5
power operator -> ** -> 10^2

Task -: 

# Scan 2 numbers form the user and do the +, /, *, -, //, ** then print the output


'''

# Operators

# c = 2 + 3
# Associativity -> Right to Left

# a + b = c

# print(c)

num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))

c = num_1 ** num_2 

# 2^3

# 3.4 < 3 -> 2.6 -> 3

print(c)

'''
string -> append(+)

namelast_name

append means the second string will get added at last position of the first string

'''