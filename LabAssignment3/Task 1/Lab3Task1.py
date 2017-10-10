# ---------------------------------------------------------------------
#   Lab Assignment 3 - Task 1
#   For any dataset, make a prediction model using Linear Regression
#   Avni Mehta, Class Id: 15
# ---------------------------------------------------------------------

# Importing libraries
import csv
import numpy as np
import matplotlib.pyplot as plt


# Read text from file into numpy arrays
def read_data(filename):
    mpg = []
    horsepower = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)          # to skip row containing column names
        for r in reader:
            mpg.append(float(r[0]))
            horsepower.append(int(r[3]))
    x = np.array(horsepower)
    y = np.array(mpg)
    return x,y


# Calculate slope and intercept for linear equation
def calculate_slope_intercept():
    x = horsepower
    y = mpg
    meanx = np.mean(x)
    meany = np.mean(y)
    xdiff = x - meanx
    ydiff = y - meany
    # Calculate the value for b1
    b1_num_array = xdiff * ydiff
    b1_den_array = xdiff * xdiff
    b1_num = b1_num_array.sum()
    b1_den = b1_den_array.sum()
    b1 = b1_num / b1_den
    # Calculate the value for b0
    b0 = meany - (b1 * meanx)
    return b1, b0


# Plot the model
def plot_model(x, y, b1, b0):
    plt.scatter(x, y, s=5)
    yhat = b1 * x + b0
    plt.plot(x, yhat, color='red')
    plt.title('Auto Dataset')
    plt.xlabel('Horsepower')
    plt.ylabel('Miles per Gallon')
    plt.show()


# Predict response(Y) for given input(X)
def predict_response(newX, b1, b0):
    print("\nPredicting mpg for horsepower = " + str(newX))
    print("Linear equation between horsepower and mpg is :: mpg = " + str(round(b1, 2)) + " * horsepower + " + str(round(b0, 2)))
    yhat = b1 * newX + b0
    print("Predicted mpg = " + str(round(yhat, 2)))

# -------------
# Main Activity
# -------------

print("\n----------------------------------------------------------------")
print("Linear Regression Model for Auto dataset")
print("Independent variable is Horsepower and Dependent variable is mpg")
print("----------------------------------------------------------------")

# Read Auto dataset into numpy arrays
# downloaded from ISL book website - http://www-bcf.usc.edu/~gareth/ISL/data.html
# predictor is horsepower & response is mpg
(horsepower, mpg) = read_data('Auto.csv')

# Calculate slope(b1) and intercept(b0)
(slope, intercept) = calculate_slope_intercept()

# Plot the model
plot_model(horsepower, mpg, slope, intercept)

# Predict response(Y) based on input(X)
predict_response(250, slope, intercept)