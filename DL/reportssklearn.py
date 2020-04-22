import tensorflow.keras as keras
import sklearn.metrics as metrics
import numpy as np

path = r'img\small'
targetSize = (64,64)

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2)
trainGenerator = trainset.flow_from_directory(
        path,
        target_size=targetSize,
        #subset = 'validation', # A enlever si on veut le jeu en entier
        color_mode="grayscale",
        batch_size=1,
        class_mode="categorical",
        )
x = []
y = []
for im in trainGenerator.filenames:
    g = trainGenerator.next()
    im = g[0][0].reshape(targetSize[0]*targetSize[1])
    label = g[1].argmax()
    x.append(im)
    y.append(label)
x = np.array(x)
y = np.array(y)
print(x.shape)
print(y.shape)

import pickle
with open("data/svm.pickle", "rb") as f:
    model = pickle.load(f)
pred = model.predict(x)

print('Confusion Matrix')
cm = metrics.confusion_matrix(y, pred)
print(cm)
print('Classification Report')
print(metrics.classification_report(y, pred))

import matplotlib.pyplot as plt
import seaborn
plt.figure(figsize = (5,5))
seaborn.heatmap(cm, annot=True, cmap=plt.cm.Blues)
plt.xlabel('True')
plt.ylabel('Predicted')
plt.show()

def plot_classification_report(cr, title='Classification report ', with_avg_total=True, cmap=plt.cm.Blues):
    lines = cr.split('\n')
    classes = []
    plotMat = []
    for line in lines[2 : -5]:
        #print(line)
        t = line.split()
        #print(t)
        classes.append(t[0])
        v = [float(x) for x in t[1: len(t) - 1]]
        #print(v)
        plotMat.append(v)

    if with_avg_total:
        aveTotal = lines[len(lines) - 1].split()
        classes.append('avg/total')
        vAveTotal = [float(x) for x in t[1:len(aveTotal) - 1]]
        plotMat.append(vAveTotal)

    plotMat = np.array(plotMat)
    plt.figure(figsize=plotMat.shape)
    seaborn.heatmap(plotMat, annot=True, cmap=cmap)
    x_tick_marks = np.arange(3)
    y_tick_marks = np.arange(len(classes))
    plt.xticks(x_tick_marks, ['precision', 'recall', 'f1-score'], rotation=45)
    plt.yticks(y_tick_marks, classes)
    plt.tight_layout()
    plt.ylabel('Classes')
    plt.xlabel('Measures')

plot_classification_report(metrics.classification_report(y, pred))
plt.show()
