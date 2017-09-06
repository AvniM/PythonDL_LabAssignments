# Program to check if a string contains all letters of the alphabet

print('\n*** Check if a string contains all letters of the alphabet ***')
myString = str(input("Enter a string: "))

# Take an empty list, for all characters of the input string,
# check if the character is alpha and is not present in the list
# When the condition satisfies, add it to the list (lower case)
# If the length of the list is 26, then it contains A-Z

myList = []

for i in range(len(myString)):
    c = myString[i].lower()
    if c.isalpha() and myList.count(c) == 0:
        myList += c

if len(myList) == 26:
    print('\nThe entered string is a Pangram as it contains all letters of the alphabet.')
elif len(myList) < 26:
    print('\nThe entered string does not contain all letters of the alphabet.')
else:
    print('Oops! Looks like something is wrong..')
