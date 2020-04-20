import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Flatten, Dense
from tensorflow.keras import applications
import json

trainset = ImageDataGenerator(rescale=1./255)

model = applications.vgg16.VGG16(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
newModel = Sequential()
for l in model.layers:
    newModel.add(l)
newModel.add(Flatten())
model = newModel
model.build()
print(model.summary())

trainGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(224, 224),
        batch_size=1,
        class_mode="categorical",
        seed=1,
        shuffle=False,
        )

bottleneck_features_train = model.predict(trainGenerator)

print("Save CSV")
trainGenerator.reset()
with open('data/vgg16bn.csv', 'w') as f:
    for item in bottleneck_features_train:
        g = trainGenerator.next()
        s = str(g[1].argmax())
        print(s)
        for i in item:
            s+=f",{str(i)}"
        s += "\n"
        f.write(s)
        #print(s, end="")




