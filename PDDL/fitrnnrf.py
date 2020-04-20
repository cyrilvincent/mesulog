import numpy as np
import sklearn
import sklearn.model_selection as ms
import pandas as pd

dataframe = pd.read_csv("data/rnnbn.csv", header=None)
print(dataframe.head())
x = dataframe.iloc[:,1:]
y = dataframe.iloc[:,0]

print(x.shape)
print(y.shape)

xtrain,xtest,ytrain,ytest = ms.train_test_split(x,y)
import sklearn.ensemble as rf
model = rf.RandomForestClassifier()
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(score)

import pickle
with open("data/rnnrf.pickle", "wb") as f:
    f.write(pickle.dumps(model))

predict = model.predict(xtest)