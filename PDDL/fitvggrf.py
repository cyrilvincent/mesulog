import sklearn.model_selection as ms
import pandas as pd

# http://accord-framework.net/docs/html/T_Accord_MachineLearning_DecisionTrees_RandomForest.htm
# https://github.com/mdabros/SharpLearning
dataframe = pd.read_csv("data/vgg16bn.csv", header=None)
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
with open("data/vggrf.pickle", "wb") as f:
    f.write(pickle.dumps(model))

predict = model.predict(xtest)