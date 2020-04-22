import tensorflow.keras as keras
import numpy as np

model = keras.models.load_model("data/vggmodel.h5")
model.summary()

img = keras.preprocessing.image.load_img("img/small/c1/img_6.jpg", target_size=(224, 224))
img = keras.preprocessing.image.img_to_array(img)
img *= 1. / 255
img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
res = model.predict(img)
print(res)
res = res[0]
print(np.argmax(res))
print((res * 100).round().astype(int))

