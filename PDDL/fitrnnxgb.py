import numpy as np
import sklearn.model_selection as ms
import pandas as pd

np.random.seed(1)
dataframe = pd.read_csv("data/rnnbn.csv", header=None)
print(dataframe.head())
x = dataframe.iloc[:,1:].values
y = dataframe.iloc[:,0].values

print(x.shape)
print(y.shape)

xtrain,xtest,ytrain,ytest = ms.train_test_split(x,y)
import xgboost
model = xgboost.XGBClassifier("logistic")
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(score)

import pickle
with open("data/rnnxgb.pickle", "wb") as f:
    f.write(pickle.dumps(model))

predict = model.predict(xtest)