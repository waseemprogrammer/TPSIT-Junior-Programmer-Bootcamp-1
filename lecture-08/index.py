# python data casting
username = str('    yousaf  ')

# python string methods

# how to access string methods

print(username.upper())
print(username.lower())

# slicing string from the beginning

print(username[:3])

# slicing string from the end

print(username[3:])

# negative indexing

print(username[-5:-2])

# modify strings

# uppercase
print(username.upper())
# lower case
print(username.lower())
# remove white space from the start of the string and end of the string
print(username.strip())
# replace string with any string 
print(username.replace("yousaf", 'Abdullah'))
# split string into list
print(username.split())

# you have to take input from the user and then do some string modifcation like convert user input into

# upper case and lower case and remove word from beginning and end

# userInput = str(input("Please Enter Your String \n"))
# userInputInUppercase = userInput.upper()
# userInputInLowerCase = userInput.lower()
# print(f"Here is Your Uppercase String: => {userInputInUppercase}")
# print(f"Here is Your LowerCase String: => {userInputInLowerCase}")

# print(username + "string " + 'is a good boy')

# string concatination 

print(username + "Welcome")