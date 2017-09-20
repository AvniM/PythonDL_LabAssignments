# Create random vector of size 15 using NumPy
# replace the maximum value by 100.

import numpy as np


def create_vector(n):
    """
    Returns a random vector of given size
    Prints the random vector and the max value in the vector
    """
    v = np.random.random((n, n))
    print('\nMy random '+ str(n) + 'x' + str(n) + ' array is...\n')
    print(v)

    print('\n--------------------------------------------------------------------\n')
    print('Maximum value in the vector = ' + str(v.max()))
    return v


def get_matrix_index(i, n):
    """
    Returns matrix index in the form of (row, column)
    Input is the indice and the size of the matrix
    """
    r = i // n
    c = i % n
    return (r, c)


def replace(v, p, x):
    """
    Returns the vector with max value updated
    v - vector to be modified
    p - position of the vector to be modified
    x - new value
    """
    i = int(p[0])
    j = int(p[1])
    v[i][j] = x
    return v


"""
Main Activity
"""

# Create vector
size = 15
myVector = create_vector(size)

# Get max value index
maxIndex = myVector.argmax()
position = get_matrix_index(maxIndex, size)
print('Maximum value at position = ' + str(position))

# Replace max value
newVector = replace(myVector, position, 100)

# Print updated vector
print('\nUpdated Vector is : \n')
print(newVector)