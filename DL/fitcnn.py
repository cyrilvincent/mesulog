import tensorflow.keras as keras
import numpy as np
import sklearn.metrics as metrics

path = r'img\small'
targetSize = (64,64)
seed = 1
batchSize = 4 #2,4,8,16

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.2) #Facultatif sur petit jeu de données
trainGenerator = trainset.flow_from_directory(
        path,
        target_size=targetSize,
        subset = 'training', #Facultatif sur petit jeu de données
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=seed
        )

validationGenerator = trainset.flow_from_directory( #Facultatif sur petit jeu de données
        path,
        target_size=targetSize,
        subset = 'validation',
        color_mode="grayscale",
        batch_size=batchSize,
        class_mode="categorical",
        seed=1
        )

#CNN
model = keras.models.Sequential()
model.add(keras.layers.Conv2D(16, (3, 3), input_shape=(64, 64, 1), padding="same")) # padding facultatif
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 32, 32, 16

model.add(keras.layers.Conv2D(32, (3, 3), padding="same"))
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 16, 16, 32

model.add(keras.layers.Conv2D(64, (3, 3), padding="same")) #32
model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
# 8, 8, 64

#Dense
model.add(keras.layers.Flatten())
# 4096

model.add(keras.layers.Dropout(0.5)) #Facultatif pour les petits jeux de données
model.add(keras.layers.Dense(64)) # Peut être augmenté avec un gros jeu de données, voir ajouter une couche
model.add(keras.layers.Dropout(0.5)) # 0.2 0.1
model.add(keras.layers.Dense(5, activation="softmax"))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(
            trainGenerator,
            epochs=20,
            validation_data=validationGenerator, #Facultatif sur petit jeu de données
    )

model.save('data/cnnmodel.h5')
predict = model.predict(validationGenerator)


