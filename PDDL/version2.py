import tensorflow as tf
import tensorflow.keras as keras
import os
import logging
import astor

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('tensorflow').setLevel(logging.FATAL)

print(tf.__version__)
print(keras.__version__)
print(astor.__version__)

model = keras.models.load_model("cnnmodel.h5")
model.summary()
