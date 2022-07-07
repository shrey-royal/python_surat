# Arithmetic Operators - +, -, *, /, **(Exponentiation), //(floor division)
# Boolean type operators -> return true or false
# comparision Operators - ==, >, <, !=, >=, <=
# Logical Operators - and, or, not

'''
types of comparision operators

== -> Equal                     -> x == y -> 2 == 3 -> False
!= -> Not Equal                 -> x != y -> 2 != 3 -> True
>  -> Greater than              -> x > y  -> 2 > 3  -> False
<  -> Less than                 -> x < y  -> 2 < 3  -> True
<= -> Less than or Equal to     -> x <= y -> 2 <= 3 -> True
>= -> Greater than or Equal to  -> x >= y -> 2 >= 3 -> False


print("(2 == 2) -> {0}".format(2==2))
print("(2 == 3) -> {0}".format(2==3))
print()

print("(2 != 2) -> {0}".format(2!=2))
print("(2 != 3) -> {0}".format(2!=3))
print()

print("(2 > 3) -> {0}".format(2>3))
print()

print("(2 < 2) -> {0}".format(2<2))
print()

print("(2 <= 2) -> {0}".format(2<=2))
print()

print("(2 >= 2) -> {0}".format(2>=2))
'''

'''
Logical Operators: (boolean type)

1) and -> return true if both the conditions are true.

true - 1
false - 0

table for and

c1  c2  result
0   0   0
0   1   0
1   0   0
1   1   1


2) or  -> returns true if one of the conditions is true

true - 1
false - 0

table for and

c1  c2  result
0   0   0
0   1   1
1   0   1
1   1   1


3) not -> reverse the results, returns true if the result is false

c1  result
1   0
0   1

'''

x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# print("(x < 5) and (y > 5) = {0}".format((x < 5) and (y > 5)))
# print("(x < 5) or (y > 5) = {0}".format((x < 5) or (y > 5)))
print("(x > 5) = {0}".format(x>5))
print("not(x > 5) = {0}".format(not(x>5)))
