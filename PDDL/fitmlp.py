import keras
import numpy as np

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2)
batchSize = 4
nbSample = 287

trainGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        subset = 'training',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

validationGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        subset = 'validation',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=(64, 64, 1)))
model.add(keras.layers.Dense(128))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(64))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(5, activation="softmax"))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
model.summary()


model.fit(trainGenerator,
          epochs=30,
          validation_data=validationGenerator,
)
model.save('mlpmodel.h5')


