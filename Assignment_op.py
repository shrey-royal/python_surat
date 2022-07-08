'''
Assignment operators-: +=, -=, *=, /=, //=, **=, =

they are used to assign values.

c = a + b
a = 2/5, b = 3 -> 5
a = a + b


a+=b -> a = a+b

'''
"""
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# c = a+b
# a = a+b # -> a+=b
a+=b

# print(a, b, c, sep=", ")
# print(a, b, sep=", ")
print("(a+=b) = {0}".format(a))
a-=b
print("(a-=b) = {0}".format(a))

"""
"""
# IDENTICAL OPERATORS -> is, is not

x = 3
y = 3

z = x

print(id(x), id(y), id(z), sep="\t")

# returns true if both the objects are same

print("ans -> ", x is y)
print("x is z -> ", x is z)
print("x is not y -> ", x is not y)

"""
"""
# CASE SESNSITIVENESS

# Membership Operators -: in, not in

Mylist = ["apple", "banana"] # -> list
fruit = "banana"
anotherFruit = "kiwi"

print("fruit is in the list? -> ", fruit in Mylist)
print("anotherFruit is in the list? -> ", anotherFruit not in Mylist)
"""

# 1356 -> binary -> decimal

# Bitwise Operators-: & (and), | (or), ! (not), << (left shift), >> (right shift)

print("1356>>2 -> ", 1356>>2)
print("1356<<2 -> ", 1356<<2)


# 2 bytes
# 1356 -> 0000 0101 0100 1100 -> 11 -> 16 bits
#  >>2 -> 0000 0001 0101 0011 -> 339
#  <<2 -> 0001 0101 0011 0000 -> 5425
# 1 byte = 8 bits