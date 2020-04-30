import tensorflow.keras as keras
import numpy as np
import sklearn.model_selection as ms

#https://docs.microsoft.com/en-us/archive/msdn-magazine/2019/march/csharp-support-vector-machines-using-csharp
path = r'img\small'
targetSize = (64,64)
seed = 1
batchSize = 4 #2,4,8,16
np.random.seed(seed)

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
trainGenerator = trainset.flow_from_directory(
        path,
        target_size=targetSize,
        color_mode="grayscale",
        batch_size=1,
        class_mode="categorical",
        seed=seed,
        shuffle=False,
        )
x = []
y = []
for im in trainGenerator.filenames:
    g = trainGenerator.next()
    im = g[0][0].reshape(64*64) # Peut être facultatif
    label = g[1].argmax()
    x.append(im)
    y.append(label)
x = np.array(x)
y = np.array(y)
print(x.shape)
print(y.shape)

xtrain,xtest,ytrain,ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
import sklearn.svm as svm
model = svm.SVC(C=0.1, kernel="linear")
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(score)

import pickle
with open("data/svm.pickle", "wb") as f:
    f.write(pickle.dumps(model))

predict = model.predict(xtest)
print(predict - ytest)