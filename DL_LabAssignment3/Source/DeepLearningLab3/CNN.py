# ---------------------------------------------------------------------
#   Lab Assignment 3 - Task 3
#   CNN for Text Classification
#   Avni Mehta, Class Id: 22
# ---------------------------------------------------------------------

# Load Dependencies
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb
from keras.callbacks import TensorBoard

# Hyper-Parameters
max_features = 5000
no_classes = 1
max_length = 100
batch_size = 32
embedding_size = 64
dropout_rate = 0.25
no_epochs = 5
no_filters = 250
kernal_size = 3
hidden_layer_size = 250

# Load IMDB Data from Keras datasets
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print('Data loaded successfully.')
print('# Train Data = ', len(x_train))
print('# Test Data = ', len(x_test))

# Data Preprocessing
print('Preprocessing Data..')
x_train = sequence.pad_sequences(x_train, maxlen=max_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_length)

# Design Neural Network Architecture with CNN
print('Building CNN Model..')

CNN_model = Sequential()
# Add Embedding layer
CNN_model.add(Embedding(max_features, embedding_size, input_length=max_length))
CNN_model.add(Dropout(dropout_rate))
# Add 1D Convolution layer 
CNN_model.add(Conv1D(no_filters, kernal_size, padding='valid', activation='relu', strides=1))
# Add Max Pooling Layer
CNN_model.add(GlobalMaxPooling1D())
# Add Hidden Dense Layer
CNN_model.add(Dense(hidden_layer_size, activation='relu'))
CNN_model.add(Dropout(dropout_rate))
# Add Output Layer
CNN_model.add(Dense(no_classes, activation='sigmoid'))

# Configure model
CNN_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# TensorBoard
tensorboard = TensorBoard('./logs/CNN')

# Train!
print('Training the model..')
CNN_model.fit(x_train, y_train, batch_size=batch_size, verbose=2, epochs=no_epochs, validation_data=(x_test, y_test), callbacks = [tensorboard])