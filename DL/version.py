import tensorflow as tf
import tensorflow.keras as keras
import astor

print(tf.__version__)
print(keras.__version__)
print(astor.__version__)

model = keras.models.load_model("data/cnnmodel.h5")
model.summary()
