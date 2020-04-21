import keras
import numpy as np
import sklearn.metrics as metrics

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2)
trainGenerator = trainset.flow_from_directory(
        path,
        target_size=targetSize,
        subset = 'training',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=seed
        )

validationGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=targetSize,
        subset = 'validation',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

#CNN
model = keras.models.Sequential()
model.add(keras.layers.Conv2D(16, (3, 3), input_shape=(64, 64, 1)))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 32, 32, 32

model.add(keras.layers.Conv2D(32, (3, 3)))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 16, 16, 32

model.add(keras.layers.Conv2D(64, (3, 3)))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 8, 8, 64

#Dense
model.add(keras.layers.Flatten())
# 4096

model.add(keras.layers.Dense(64))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(5, activation="softmax"))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(
            trainGenerator,
            epochs=20,
            validation_data=validationGenerator,
    )


model.save('data/cnnmodel.h5')


