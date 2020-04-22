import sklearn.model_selection as ms
import pandas as pd
import numpy as np

np.random.seed(1)
dataframe = pd.read_csv("data/vgg16bn.csv", header=None)
print(dataframe.head())
x = dataframe.iloc[:,2:].values
y = dataframe.iloc[:,1].values

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
    pickle.dump(model, f)

predict = model.predict(xtest)
print(predict - ytest)