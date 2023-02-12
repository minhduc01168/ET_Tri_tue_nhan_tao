import tensorflowjs as tfjs
import os
from keras.models import load_model

os.mkdir('ann_js')
my_model = load_model("model.h5")
tfjs.converters.save_keras_model(my_model, 'ann_js')