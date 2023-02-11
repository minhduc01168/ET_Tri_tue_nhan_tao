# Import the library
import pandas as pd
import numpy as np
import matplotlib . pyplot as plt
# Data Preprocessing
from sklearn.model_selection import train_test_split
# Make the ANN!
# Importing the Keras libraries and packages
import keras
import tensorflow as tf


# Import the dataset
df = pd.read_csv('credit_risk_dataset_normalization.csv')
X = pd.DataFrame(df)
X = X.drop(['loan_status'], axis=1)
y = df[['loan_status']]
# X_train , X_test , y_train , y_test = train_test_split (X, y, test_size = 0.2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.16, random_state=1)
# Initialize Sequential object
ann = tf.keras.models.Sequential()

# Total no. of Neurons = 6
# We will be adding 2 hidden layers in our Neural Network
ann.add(tf.keras.layers.Dense(units=11, activation='relu',input_dim = np.shape( X_test )[1]))
ann.add(tf.keras.layers.Dense(units=25, activation='relu'))
ann.add(tf.keras.layers.Dense(units=10, activation='relu'))
ann.add(tf.keras.layers.Dense(units=5, activation='relu'))
# Adding Output Later
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# Initializing our Compiler
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# Train our model
# ann.fit(X_train, y_train, batch_size=128, epochs=150, verbose=1)
history = ann.fit(X_train, y_train, epochs=150, batch_size=32, validation_data=(X_val, y_val))
# batch size = the number of training examples in one forward/backward pass. The higher the batch size, the more memory space you'll need.
ann.save('model.h5')
print("Finish model!")
# y_pred = ann.predict(X_test)
# y_pred = (y_pred > 0.5)   # This will predict output values as 'True' and 'False'
# print(y_pred)