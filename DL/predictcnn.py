import tensorflow.keras as keras
import numpy as np
import tensorflow as tf
import io
import h5py

print(tf.__version__)
model = keras.models.load_model("data/cnnmodel.h5")
# with open("data/cnnmodel.h5", "rb") as f:
#     bio = io.BytesIO(f.read())
#     h = h5py.File(bio,'r')
#     model = keras.models.load_model(h)
model.summary()

#img = keras.preprocessing.image.load_img("img/small/c1/img_6.jpg", target_size=(64, 64), color_mode="grayscale") #CNN
img = keras.preprocessing.image.load_img("img/small/c1/img_6.jpg", target_size=(224, 224)) #VGG
img = keras.preprocessing.image.img_to_array(img)
img *= 1. / 255
img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
res = model.predict(img)
print(res)
res = res[0]
print(np.argmax(res))
print((res * 100).round().astype(int))

# import matplotlib.pyplot as plt
# plt.bar(np.arange(len(res)) + 1, res)
# plt.show()

