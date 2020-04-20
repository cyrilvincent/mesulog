import numpy as np
import tensorflow.keras as keras
from PIL import Image

im = Image.open("data/test4.png", )
im = im.resize((224,224))
im = np.asarray(im)
print(im.shape)
im = im.reshape(1,224,224,3) / 255

model = keras.applications.vgg16.VGG16(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
newModel = keras.Sequential()
for l in model.layers:
    newModel.add(l)
newModel.add(keras.layers.Flatten())
model = newModel
model.build()

bn = model.predict(im,1)[0]
bn = bn.reshape(1,25088)

import pickle
with open("data/vggsvm.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(bn)
print(predict)
with open("data/vggrf.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(bn)
print(predict)

with open("data/vggxgb.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(bn)
print(predict)


