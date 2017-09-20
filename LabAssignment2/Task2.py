# Generate a dictionary that contains (k, k*k) .
# Print the dictionary generated and the series should include both 1 and k

def get_input():
    """
    Get input from the user.
    """
    return int(input('\nEnter number of elements : '))

def create_print_dict(n):
    """
    Creates a dictionary of n elements with KV pair as (k : k*k)
    """
    if n == 0:
        print('\nThe dictionary with 0 elements is an empty dictionary.')
    else:
        myDict = {}
        for i in range(n):
            k = i+1
            myDict[k] = k*k
        print('\nThe dictionary is created as follows:')
        print(myDict)

# ---------------
# Main Activity
# ---------------
print('\nFor n number of elements, this program will create a dictionary')
print('with KV pair as (k : k*k) where k ranges from 1 to n')
create_print_dict(get_input())

while input('\nDo you want to create another dictionary? Enter Y or N : \n')[0].lower() == 'y':
    create_print_dict(get_input())

print('\nOkay, Adios!')