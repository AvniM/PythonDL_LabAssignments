# ---------------------------------------------------------------------
#   Lab Assignment 3 - Task 3
#   Implement SVM Classification for Linear Kernel and RBF Kernel
#   Avni Mehta, Class Id: 15
# ---------------------------------------------------------------------

# Importing Libraries
from sklearn.cross_validation import train_test_split
from sklearn import datasets, metrics, svm

# Setting dataset name
dataset_name = 'Breast Cancer dataset'

print('\n----------------------------------------------------------------')
print('Implementing SVM Classification for Linear Kernel and RBF Kernel')
print('For '+ dataset_name + ' from sklearn')
print('----------------------------------------------------------------')

# Loading Dataset - Breast Cancer dataset from sklearn
cancerdataset = datasets.load_breast_cancer()

# Getting the data and response of the dataset
x = cancerdataset.data
y = cancerdataset.target

# Splitting the dataset into training (75%) and test (25%)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

# ----------------------------
# Applying linear kernel model
# ----------------------------
linearmodel = svm.SVC(kernel='linear')

# Fitting the model for training data
linearmodel.fit(x_train, y_train)
print('\nCase 1. Applying linear kernel model on training data (75%)')

# Predicting the response for test data
y_pred_linear = linearmodel.predict(x_test)
print('        Predicting response for test data (25%)')

# Getting accuracy for linear model
linear_accuracy = metrics.accuracy_score(y_test,y_pred_linear)
print('        Accuracy for linear kernel model is ' + str(round(linear_accuracy, 4)))

# ----------------------------
# Applying RBF kernel model
# ----------------------------
rbfmodel = svm.SVC(kernel='rbf')

# Fitting the model for training data
rbfmodel.fit(x_train, y_train)
print('\nCase 2. Applying RBF kernel model on training data (75%)')

# Predicting the response for test data
y_pred_rbf = rbfmodel.predict(x_test)
print('        Predicting response for test data (25%)')

# Getting accuracy for linear model
rbf_accuracy = metrics.accuracy_score(y_test,y_pred_rbf)
print('        Accuracy for RBF kernel model is ' + str(round(rbf_accuracy, 4)))

# Comparing accuracy for both models
if linear_accuracy > rbf_accuracy:
    print('\nLinear Kernel model has better accuracy over RBF Kernel model for ' + dataset_name + '.')
    print('So, Linear kernel model is better for ' + dataset_name + '.')
elif linear_accuracy < rbf_accuracy:
    print('\nRBF Kernel model has better accuracy over Linear Kernel model for ' + dataset_name + '.')
    print('So, RBF kernel model is better for ' + dataset_name + '.')
else:
    print('\nLinear Kernel model has same accuracy as RBF Kernel model for ' + dataset_name + '.')