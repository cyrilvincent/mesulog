import keras
import numpy as np
import sklearn.model_selection as ms

#https://docs.microsoft.com/en-us/archive/msdn-magazine/2019/march/csharp-support-vector-machines-using-csharp

np.random.seed(1)
trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
trainGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        color_mode="grayscale",
        batch_size=1,
        class_mode="categorical",
        seed=1,
        shuffle=False,
        )
x = []
y = []
i = 0
for g in trainGenerator:
    im = g[0][0].reshape(64*64)
    label = g[1].argmax()
    x.append(im)
    y.append(label)
    i+=1
    if i == 264:
        break
x = np.array(x)
y = np.array(y)
print(x.shape)
print(y.shape)

xtrain,xtest,ytrain,ytest = ms.train_test_split(x,y)
import sklearn.svm as svm
model = svm.SVC(C=0.1, kernel="linear")
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(score)

import pickle
with open("data/svm.pickle", "wb") as f:
    f.write(pickle.dumps(model))

predict = model.predict(xtest)
print(predict)