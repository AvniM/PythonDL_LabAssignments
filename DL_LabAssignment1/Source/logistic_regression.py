# ----------------------------------------------------------------------------
#  * CS5590: Deep Learning - Lab Assignment 1
#  * Logistic Regression for IRIS dataset using tensorflow
#  * Class Id #22: Avni Mehta
# ----------------------------------------------------------------------------

# Import Libraries
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Step 1: Load the data
df = pd.read_csv('Iris.csv')

# Step 2: Data preprocessing
# Drop ID column
df = df.drop('Id', axis=1)

# Convert Species name to numerical value 
# Iris-setosa -> 1, Iris-versicolor -> 2, Iris-virginica -> 3
df['Species'] = df['Species'].replace(['Iris-setosa', 'Iris-versicolor','Iris-virginica'], [1, 2, 3])

# X : features, y : labels
X = df.loc[:, ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df.loc[:, ['Species']]

# Convert features and labels to one-hot encoding
oneHot = OneHotEncoder()
oneHot.fit(X)
X = oneHot.transform(X).toarray()
oneHot.fit(y)
y = oneHot.transform(y).toarray()

# Step 3: Split data into 80-20 training-testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 4:  Define parameters for the model
learning_rate = 0.001
num_epochs = 150

# Step 5: Create placeholders for features and labels
X = tf.placeholder(tf.float32, [None, 15])
y = tf.placeholder(tf.float32, [None, 3])

# Step 6: Create weights and bias, initialized to 0
w = tf.Variable(tf.zeros([15, 3]))
b = tf.Variable(tf.zeros([3]))

# Step 7: Predict y from X, w and b
y_pred = tf.nn.softmax(tf.add(tf.matmul(X, w), b))

# Step 8: Define loss function
# use softmax cross entropy with logits as the loss function
loss = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_pred)

# Step 9: Define training optimizer
# using gradient descent with learning rate of 0.001 to minimize cost
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

init = tf.global_variables_initializer()

# Start tensorflow session
with tf.Session() as sess:

    # initialize all variables
    sess.run(init)

    # Write summary for generating graph
    writer = tf.summary.FileWriter('./graphs/logistic_reg', sess.graph)

    # Step 10: Training the model
    for epoch in range(num_epochs):
        total_loss = 0
        _, l = sess.run([optimizer, loss], feed_dict={X: X_train, y: y_train})
        total_loss += l
        print("Epoch: {}".format(epoch + 1), "loss = {}".format(total_loss))

    writer.close()
    print("Optimization Complete!\n")

    # Step 11: Testing the model
    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy:", accuracy.eval({X: X_test, y: y_test}))
