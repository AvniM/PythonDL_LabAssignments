# Find numbers divisible by 5 and multiple of 2, between 700 and 1700

print('\n*** Find numbers between 700-1700 that are divisible by 5 and multiple of 2 ***')

min = 700
max = 1700

myList = []

# If n % 5 is 0, then its divisible by 5
# If n % 2 is 0, and n >= 2, then its a multiple of 2
# Since the numbers range from 700 to 1700, its implied that n >=2

for i in range(min, max+1):
    if i%5 == 0 and i%2 == 0:
        myList.append(i)

print('\nThere are ' + str(len(myList)) + ' numbers between 700-1700 that are divisible by 5 and multiple of 2.')
print('\nThose numbers are..')
print(myList)