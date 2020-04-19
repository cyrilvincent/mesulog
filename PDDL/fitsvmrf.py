import numpy as np
import sklearn
import sklearn.model_selection as ms
import pandas as pd

dataframe = pd.read_csv("vgg16-bottleneck-train.csv")
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