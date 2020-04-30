from PIL import Image
import numpy as np

#https://docs.microsoft.com/en-us/archive/msdn-magazine/2019/march/csharp-support-vector-machines-using-csharp
im = Image.open("data/test2.png", ).convert('L')
im = np.asarray(im)
print(im.shape)
im = im.reshape(1,64*64) / 255
import pickle
with open("data/svm.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(im)
print(predict)
with open("data/rf.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(im)
print(predict)
with open("data/xgb.pickle", "rb") as f:
    model = pickle.loads(f.read())
predict = model.predict(im)
print(predict)