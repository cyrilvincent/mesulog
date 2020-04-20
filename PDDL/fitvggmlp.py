import tensorflow.keras as keras

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2)

model = keras.applications.vgg16.VGG16(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
newModel = keras.models.Sequential()
for l in model.layers:
    newModel.add(l)
newModel.add(keras.layers.Flatten())
newModel.add(keras.layers.Dense(64, activation="relu"))
newModel.add(keras.layers.Dropout(0.5))
newModel.add(keras.layers.Dense(5, activation="softmax"))
model = newModel

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

print(model.summary())

batchSize = 4
trainGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(224, 224),
        subset = 'training',
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

validationGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(224, 224),
        subset = 'validation',
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

model.fit(
            trainGenerator,
            epochs=30,
            validation_data=validationGenerator,
    )

model.save('vggmodel.h5')



