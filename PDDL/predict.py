import tensorflow as tf
import tensorflow.keras as keras
import os
import logging
import astor
import PIL

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('tensorflow').setLevel(logging.FATAL)

print(tf.__version__)
print(keras.__version__)
print(astor.__version__)
print(PIL.PILLOW_VERSION)

model = keras.models.load_model("cnnmodel.h5")
model.summary()

img = keras.preprocessing.image.load_img("test5.png", target_size=(64, 64), color_mode="grayscale")
img = keras.preprocessing.image.img_to_array(img)
img *= 1. / 255
img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
res = model.predict(img)
print(res)

