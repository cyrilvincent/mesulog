import tensorflow.keras as keras
import numpy as np
import sklearn.metrics as metrics

seed = 1
path = r'img\small'
targetSize = (224,224)
batchSize = 16

model = keras.models.load_model('data/vggmodel.h5')

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2)
validationGenerator = trainset.flow_from_directory(
        path,
        target_size=targetSize,
        #subset = 'validation', # A enlever si on veut le jeu en entier
        batch_size=batchSize,
        class_mode="categorical",
        seed=seed,
        shuffle=False, #important, ordre alphabetique
        )
pred = model.predict(validationGenerator)
pred = np.argmax(pred, axis=1)
print('Confusion Matrix')
cm = metrics.confusion_matrix(validationGenerator.classes, pred)
print(cm)
print('Classification Report')
print(metrics.classification_report(validationGenerator.classes, pred))

import matplotlib.pyplot as plt
import seaborn
plt.figure(figsize = (5,5))
seaborn.heatmap(cm, annot=True, cmap=plt.cm.Blues)
plt.xlabel('True')
plt.ylabel('Predicted')
plt.show()

def plot_classification_report(cr, title='Classification report', with_avg_total=True, cmap=plt.cm.Blues):
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
