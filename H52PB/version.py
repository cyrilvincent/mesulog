import tensorflow as tf
import tensorflow.keras as keras
print(tf.__version__)
print(keras.__version__)

model = keras.models.load_model("cnnmodel.h5")
model.summary()
