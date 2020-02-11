import keras
import numpy as np

class TwoImageGenerator(keras.utils.Sequence):

    def __init__(self, generator1, generator2):
        self.generator1 = generator1
        self.generator2 = generator2

    def __getitem__(self, i):
        X1i = self.generator1[i]
        X2i = self.generator2[i]
        imgFirst = X1i[0]
        imgSecond = X2i[0]
        imgi = np.zeros((len(imgFirst), 64, 64, 2), dtype=np.float32)
        for n in range(0, len(imgFirst)):
            img1 = imgFirst[n]
            img2 = imgSecond[n]
            imgi[n] = np.dstack((img1, img2))
        return imgi, X2i[1]

    def __len__(self):
        return len(self.generator1)


trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2)
#validationset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
batchSize = 4
nbSample = 287

# Image with 2 channels : https://github.com/keras-team/keras/issues/3416
# https://stackoverflow.com/questions/49404993/keras-how-to-use-fit-generator-with-multiple-inputs

trainGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        subset = 'training',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

trainGenerator2 = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        subset = 'training',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

# validationGenerator = validationset.flow_from_directory(
#         r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\validation\cyril',
#         target_size=(64, 64),
#         color_mode="grayscale",
#         class_mode="categorical",
#         batch_size=batchSize)

validationGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        subset = 'validation',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

validationGenerator2 = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        subset = 'validation',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

import numpy as np
def twoImageGenerator(generator1, generator2):
    while True:
        X1i = generator1.next()
        X2i = generator2.next()
        imgFirst = X1i[0]
        imgSecond = X2i[0]
        imgi = np.zeros((len(imgFirst), 64, 64, 2), dtype=np.float32)
        for n in range(0, len(imgFirst)):
            img1 = imgFirst[n]
            img2 = imgSecond[n]
            imgi[n] = np.dstack((img1, img2))
        yield imgi, X2i[1]  # Yield both images and their mutual label

#CNN
model = keras.models.Sequential()
model.add(keras.layers.Conv2D(16, (3, 3), input_shape=(64, 64, 2)))
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 32, 32, 32

model.add(keras.layers.Conv2D(32, (3, 3)))
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 16, 16, 32

model.add(keras.layers.Conv2D(64, (3, 3)))
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 8, 8, 64

#Dense
model.add(keras.layers.Flatten())
# 4096
model.add(keras.layers.Dense(64, activation="relu"))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(5, activation="softmax"))

#sgd = keras.optimizers.SGD(lr=0.0001, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              #optimizer=sgd,
              metrics=['accuracy'])

# model.fit_generator(
#         trainGenerator,
#         steps_per_epoch=nbSample // batchSize,
#         epochs=30,
#         validation_data=validationGenerator,
#         validation_steps=validationSize // batchSize
# )

# model.fit(
#             trainGenerator,
#             epochs=30,
#             validation_data=validationGenerator,
#     )

model.fit(
            TwoImageGenerator(trainGenerator, trainGenerator2),
            epochs=30,
            validation_data=TwoImageGenerator(validationGenerator, validationGenerator2),
            # steps_per_epoch=nbSample // batchSize,
            # validation_steps=(nbSample * 0.2) // batchSize
    )

# Other method
#PIL Merge
# from PIL import Image
# imr = Image.open("rpath")
# img =  Image.open("gpath")
# imb = Image.open("bpath")
# im = Image.merge("RGB", (imr, img, imb))
# im.save("rgbpath")


model.save('cnnmodel.h5')


