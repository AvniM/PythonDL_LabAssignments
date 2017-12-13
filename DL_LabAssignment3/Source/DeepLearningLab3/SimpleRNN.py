# ---------------------------------------------------------------------
#   Lab Assignment 3 - Task 1
#   Simple RNN for Text Classification
#   Avni Mehta, Class Id: 22
# ---------------------------------------------------------------------

# Load Dependencies
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, SimpleRNN
from keras.datasets import imdb
from keras.callbacks import TensorBoard

# Hyper-Parameters
max_features = 5000
no_classes = 1
max_length = 100
batch_size = 64
embedding_size = 64
dropout_rate = 0.5
hidden_layer_size = 250
no_epochs = 5

# Load IMDB Data from Keras datasets
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print('Data loaded successfully.')
print('# Train Data = ', len(x_train))
print('# Test Data = ', len(x_test))

# Data Preprocessing
print('Preprocessing Data..')
x_train = sequence.pad_sequences(x_train, maxlen=max_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_length)

# Design Neural Network Architecture with SimpleRNN
print('Building Simple RNN Model..')

RNN_model = Sequential()
# Add Embedding layer
RNN_model.add(Embedding(max_features, embedding_size, input_length=max_length))
RNN_model.add(Dropout(dropout_rate))
# Add Simple RNN layer
RNN_model.add(SimpleRNN(input_dim=1, output_dim=25, batch_input_shape=(1, 3)))
# Add Dense Hidden Layer
RNN_model.add(Dense(hidden_layer_size, activation='relu'))
RNN_model.add(Dropout(dropout_rate))
# Output Layer 
RNN_model.add(Dense(no_classes, activation='sigmoid'))

# Configure model
RNN_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# TensorBoard
tensorboard = TensorBoard('./logs/SimpleRNN')

# Train!
print('Training the model..')
RNN_model.fit(x_train, y_train, batch_size=batch_size, verbose=2, epochs=no_epochs, validation_data=(x_test, y_test), callbacks = [tensorboard])