# python tuples

car = ("Maruti", 2023,"licensed", 2023)

print(car)

# items

print(car[1])

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


print(len(car))

person = ("Ghazi",)

print(type(person))

# tuple constructor

abdullah = tuple(('ab',22,'msc'))
# abdullah = list(('ab',22,'msc'))
# abdullah[0] = "Abdullah"
person = list(abdullah)
person[0] = "Abdullah"
abdullah = tuple(person)
print(abdullah)