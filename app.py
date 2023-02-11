import pickle
from flask import Flask, render_template, url_for, request
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.metrics import cohen_kappa_score

model = pickle.load(open('model.h5', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():





if __name__ == '__main__':
    app.run(debug=True)