import numpy as np
import tensorflow.keras as keras
from PIL import Image

im = Image.open("data/test3.png", )
im = im.resize((299,299))
im = np.asarray(im)
print(im.shape)
im = im.reshape(1,299,299,3) / 255

model = keras.applications.inception_resnet_v2.InceptionResNetV2(include_top=False, weights="imagenet", input_shape=(299, 299, 3))
x = model.output
x = keras.layers.Flatten()(x)
model = keras.models.Model(inputs=model.input, outputs=x)

bn = model.predict(im,1)[0]
bnv = bn
bn = bn.reshape(1,bn.shape[0])

import pickle
with open("data/rnnsvm.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(bn)
print(predict)
with open("data/rnnrf.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(bn)
print(predict)

import pandas as pd
bn = bnv
bn = np.insert(bn,0,np.nan)
bn = pd.DataFrame(bn.reshape(1,len(bn))).iloc[:,1:]
with open("data/rnnxgb.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(bn)
print(predict)

