# list constructor 

fruits = list(("apple", "banana", "cherry", "apple"))

# change list item

# fruits[1] = 'Orange'
# print(fruits)

# check if item exitsts in the list

# if "random" in fruits:
#     print("yes Apple is founded in list")
# else:
#     print("Sorryy Appple isn't in the list")
    
# Change a Range of Item Values

# fruits[1:5] = ["blackcurrant", "watermelon", "Otehr", 'koi nahi', 'p', 'o', 3904]

# print(fruits)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# fruits.insert(1, 'okay')
# print(fruits)


# Python - Add List Items

# fruits.append("orange")

# print(fruits)

# Extend List
# To append elements from another list to the current list, use the extend() method.

# autumn_Weather = list(("mango", "banna", "santra"))

# fruits.extend(autumn_Weather)

# print(fruits)

# automn_Weather = ("mango", 'banana', 'santra')
# print(type(automn_Weather))
# fruits.extend(automn_Weather)
# print(type(fruits))
# print(fruits)


# Remove Specified Item from the list , and it will remove first occurances

# fruits.remove('apple')

# print(fruits)

# Remove Specified Index
# The pop() method removes the specified index.

# fruits.pop(-1)

# print(fruits)

# If you do not specify the index, the pop() method removes the last item.

# fruits.pop()

# print(fruits)

# The del keyword also removes the specified index:

# del fruits

# print(fruits)

# Clear the List
# The clear() method empties the list.

# fruits.clear()
# print(fruits)

# del fruits
# print(fruits)