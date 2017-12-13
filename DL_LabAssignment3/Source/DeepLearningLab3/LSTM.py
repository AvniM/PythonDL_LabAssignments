# ---------------------------------------------------------------------
#   Lab Assignment 3 - Task 2
#   LSTM for Text Classification
#   Avni Mehta, Class Id: 22
# ---------------------------------------------------------------------

# Set seed
import numpy as np
np.random.seed(42)

# Load Dependencies
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional
from keras.datasets import imdb
from keras.callbacks import TensorBoard

# Hyper-Parameters
max_features = 5000
no_classes = 1
max_length = 100
batch_size = 32
embedding_size = 64
dropout_rate = 0.5
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
y_train = np.array(y_train)
y_test = np.array(y_test)

# Design Neural Network Architecture with LSTM
print('Building LSTM Model..')

LSTM_model = Sequential()
# Add Embedding layer
LSTM_model.add(Embedding(max_features, embedding_size, input_length=max_length))
# Add Bidirectional LSTM Layer
LSTM_model.add(Bidirectional(LSTM(64)))
LSTM_model.add(Dropout(dropout_rate))
# Output Layer 
LSTM_model.add(Dense(no_classes, activation='sigmoid'))

# Configure model
LSTM_model.compile('adam', 'binary_crossentropy', metrics=['accuracy'])

# TensorBoard
tensorboard = TensorBoard('./logs/LSTM')

# Train!
print('Training the model..')
LSTM_model.fit(x_train, y_train, batch_size=batch_size, verbose=2, epochs=no_epochs, validation_data=[x_test, y_test], callbacks = [tensorboard])