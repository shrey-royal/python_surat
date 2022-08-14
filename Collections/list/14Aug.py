# Access List Items

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "papaya", "peach", "pear", "plum", "watermelon", "pineapple", "strawberry", "tomato"]

print(fruits[0])    # -> list is indexed or ordered collection
# index always starts from 0

print(fruits[6:9])  # -> print the elements from index 6 to index 9

print(fruits[3:9:2]) # -> print the elements from index 3 to index 9 with a step of 2

# i want to check that if the element entered by the user is in the list or not



if "strawberry" in fruits:
    print("Yes, 'Strawberry' is in the list")
else:
    print("No, 'Strawberry' is not in the list")