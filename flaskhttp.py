import tensorflow as tf
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import numpy as np
from keras.models import load_model

my_model = tf.keras.models.load_model("model.h5")

#######HTTP SERVER###############################################################################
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin(origin = '*')
def index():
    return "Sever is running!"

if __name__ =='__main__':
    app.run(debug=True, port= 8000)