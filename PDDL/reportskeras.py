import tensorflow.keras as keras
import numpy as np
import sklearn.metrics as metrics

model = keras.models.load_model('data/cnnmodel.h5')

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
validationGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        color_mode="grayscale",
        batch_size=1,
        class_mode="categorical",
        seed=1,
        shuffle=False,
        )
pred = model.predict(validationGenerator)
pred = np.argmax(pred, axis=1)
print('Confusion Matrix')
cm = metrics.confusion_matrix(validationGenerator.classes, pred)
print(cm)
print('Classification Report')
print(metrics.classification_report(validationGenerator.classes, pred))

# cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
# cm = (cm * 100).astype(int)

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

plot_classification_report(metrics.classification_report(validationGenerator.classes, pred))
plt.show()
