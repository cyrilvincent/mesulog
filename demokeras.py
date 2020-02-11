import keras

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2)
#validationset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
batchSize = 4
nbSample = 287
# validationSize = 260

# Image with 2 channels : https://github.com/keras-team/keras/issues/3416
# https://stackoverflow.com/questions/49404993/keras-how-to-use-fit-generator-with-multiple-inputs

trainGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(64, 64),
        subset = 'training',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
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
        )

#CNN
model = keras.models.Sequential()
model.add(keras.layers.Conv2D(16, (3, 3), input_shape=(64, 64, 1)))
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

model.fit(
            trainGenerator,
            epochs=30,
            validation_data=validationGenerator,
    )

model.save('cnnmodel.h5')


