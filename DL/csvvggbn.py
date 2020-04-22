import tensorflow.keras as keras

path = r'img\small'
targetSize = (224,224)
seed = 1

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

model = keras.applications.vgg16.VGG16(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
newModel = keras.Sequential()
for l in model.layers:
    newModel.add(l)
newModel.add(keras.layers.Flatten())
model = newModel
model.build()
print(model.summary())

trainGenerator = trainset.flow_from_directory(
        path,
        target_size=targetSize,
        batch_size=1,
        class_mode="categorical",
        seed=seed,
        shuffle=False,
        )

bn = model.predict(trainGenerator)

print("Save CSV")
trainGenerator.reset()
ix = 0
with open('data/vgg16bn.csv', 'w') as f:
    for item in bn:
        g = trainGenerator.next()
        s = trainGenerator.filenames[ix]
        ix+=1
        s += f",{g[1].argmax()}"
        print(s)
        for i in item:
            s+=f",{str(i)}"
        s += "\n"
        f.write(s)
        #print(s, end="")

import csv
with open("data/vgg16bn.csv") as f:
    l = list(csv.reader(f))
    print(len(l))




