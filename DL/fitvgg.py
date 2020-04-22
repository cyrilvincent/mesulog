import tensorflow.keras as keras

path = r'img\small'
targetSize = (224,224)
seed = 1
batchSize = 4 #2,4,8,16

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2) #Facultatif sur petit jeu de données
trainGenerator = trainset.flow_from_directory(
        path,
        target_size=targetSize,
        subset = 'training', #Facultatif sur petit jeu de données
        batch_size=batchSize,
        class_mode="categorical",
        seed=seed
        )

validationGenerator = trainset.flow_from_directory( #Facultatif sur petit jeu de données
        path,
        target_size=targetSize,
        subset = 'validation',
        batch_size=batchSize,
        class_mode="categorical",
        seed=seed
        )

model = keras.applications.vgg16.VGG16(include_top=False, weights="imagenet", input_shape=(224, 224, 3))
newModel = keras.Sequential()
for l in model.layers:
    l.trainable=False
    newModel.add(l)
newModel.add(keras.layers.Flatten())
model = newModel
model.add(keras.layers.Dropout(0.5)) #Facultatif pour les petits jeux de données
model.add(keras.layers.Dense(256)) # Peut être augmenté avec un gros jeu de données, voir ajouter une couche
model.add(keras.layers.Dropout(0.5)) #Facultatif pour les petits jeux de données
model.add(keras.layers.Dense(64)) # Peut être augmenté avec un gros jeu de données, voir ajouter une couche
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(5, activation="softmax"))

model.build()
print(model.summary())
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(
            trainGenerator,
            epochs=20,
            validation_data=validationGenerator, #Facultatif sur petit jeu de données
    )

model.save('data/vggmodel.h5')
predict = model.predict(validationGenerator)


