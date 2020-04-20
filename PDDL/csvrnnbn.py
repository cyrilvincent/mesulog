import tensorflow.keras as keras

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

model = keras.applications.inception_resnet_v2.InceptionResNetV2(include_top=False, weights="imagenet", input_shape=(299, 299, 3))
x = model.output
x = keras.layers.Flatten()(x)
model = keras.models.Model(inputs=model.input, outputs=x)
print(model.summary())

trainGenerator = trainset.flow_from_directory(
        r'C:\Users\conta\CVC\ATP\Mesulog\191219_baseImages_tester\_BaseReference',
        target_size=(299, 299),
        batch_size=1,
        class_mode="categorical",
        seed=1,
        shuffle=False,
        )

bottleneck_features_train = model.predict(trainGenerator)

print("Save CSV")
trainGenerator.reset()
with open('data/rnnbn.csv','w') as f:
    for item in bottleneck_features_train:
        g = trainGenerator.next()
        s = str(g[1].argmax())
        print(s)
        for i in item:
            s+=f",{str(i)}"
        s += "\n"
        f.write(s)
        #print(s, end="")




