# Write a program that accepts a sentence as input and remove duplicate words .
# Sort them alphanumerically and print it.


def get_input():
    """
    Get input from the user.
    If the user provides non-alphanumeric input, it wont be printed in the output
    """
    return input('\nEnter a sentence (alphanumeric only): ')


def split_and_print(text):
    """
    Splits the given text into words. Adds the words to a set,
    set handles duplicates automatically. Prints the set values separated by space
    """
    mySet = set()

    for i in range(len(text.split())):
        word = text.split()[i]
        # Replace special characters in a sentence
        word = word.replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace('\n', '')
        # add to the set only if it is alphanumeric.
        # Doesn't add words having special characters
        if word.isalnum():
            mySet.add(word.lower())

    if len(mySet) == 0:
        print('\nThere are no alphanumeric words in the given sentence.')
    else:
        print('\nThe given sentence is sorted and duplicates have been removed...')
        print('Output : ' + ' '.join(sorted(mySet)))


# ---------------
# Main Activity
# ---------------
print('-----------------------------------------------------')
print('This program splits the words in the given sentence,')
print('and prints the unique words in sorted order..')
print('-----------------------------------------------------')
myText = get_input()
split_and_print(myText)

# Run the program until the user wants to quit
while input('\nDo you want to sort another sentence? Enter Y or N : \n')[0].lower() == 'y':
    myText = get_input()
    split_and_print(myText)

print('\nOkay, Adios!')