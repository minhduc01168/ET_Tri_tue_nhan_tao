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
from keras.models import load_model

# load model da train
my_model = load_model("model.h5")

# Predict
list_input=[[0.192308, 0.141803, 1.000000, 0.0625, 0.8, 0.25, 0.184502, 0.391850, 0.340426, 0.0, 0.000000]]
df_input = pd.DataFrame (list_input, columns = ['person_age', 'person_income','person_home_ownership', 'person_emp_length', 'loan_intent', 'loan_grade', 'loan_amnt', 'loan_int_rate','loan_percent_income', 'cb_person_default_on_file', 'cb_person_cred_hist_length'])
y_pred = my_model.predict(df_input)
y_pred = (y_pred > 0.5)   # This will predict output values as 'True' and 'False'
print(y_pred)