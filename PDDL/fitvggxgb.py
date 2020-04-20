import sklearn.model_selection as ms
import pandas as pd
import numpy as np

# https://github.com/mdabros/SharpLearning

np.random.seed(1)
dataframe = pd.read_csv("data/vgg16bn.csv", header=None)
print(dataframe.head())
x = dataframe.iloc[:,1:].values # XGB Pandas Index PB
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
with open("data/vggxgb.pickle", "wb") as f:
    f.write(pickle.dumps(model))

predict = model.predict(xtest)