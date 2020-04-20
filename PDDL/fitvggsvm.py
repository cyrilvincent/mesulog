import numpy as np
import sklearn
import sklearn.model_selection as ms
import pandas as pd

dataframe = pd.read_csv("data/vgg16bn.csv")
print(dataframe.head())
x = dataframe.iloc[:,1:]
y = dataframe.iloc[:,0]

print(x.shape)
print(y.shape)

xtrain,xtest,ytrain,ytest = ms.train_test_split(x,y)
import sklearn.svm as svm
model = svm.SVC(C=0.1, kernel="linear")
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(score)

import pickle
with open("data/vggsvm.pickle", "wb") as f:
    f.write(pickle.dumps(model))

predict = model.predict(xtest)