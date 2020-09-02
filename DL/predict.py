import tensorflow.keras as keras
import tensorflow as tf
import io
import h5py
import Crypto.Cipher.AES as aes  #pip install pycryptodome
import argparse
import os

#pip install pyarmor
#pip install pyinstaller

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

copyright = b"Mesulog 2020"
dev = b'Cyril Vincent'

def load_image(path, grayscale=False):
    if grayscale:
        im = keras.preprocessing.image.load_img(path, target_size=(224, 224), color_mode="grayscale")
    else:
        print(f"Analyse {path}")
        im = keras.preprocessing.image.load_img(path, target_size=(224, 224))
    im = keras.preprocessing.image.img_to_array(im)
    im *= 1. / 255
    im = im.reshape((1, im.shape[0], im.shape[1], im.shape[2]))
    return im

def load_model(name):
    nonce = b'\xa1TD\xdc\xde\x0b\xfc\xc8\xa1\xdc()DuZb'
    key = copyright[:8] + b'& ' + dev[:5] + b'!'
    with open(name, "rb") as f:
        data = f.read()
        cipher = aes.new(key, aes.MODE_EAX, nonce=nonce)
        data = cipher.decrypt(data)
        bio = io.BytesIO(data)
        h = h5py.File(bio,'r')
        model = keras.models.load_model(h)
        return model

def load_and_predict(name, im, grayscale=False):
    model = load_model(name)
    img = load_image(im, grayscale)
    return model.predict(img)[0]

def to_csv(res):
    print("Generate output.csv")
    with open("output.csv","w") as f:
        f.write("model,void,particle,floating_potential,protusion,surface_defection,external_noise\n")
        nrow = 0
        for row in res:
            if nrow == 0:
                f.write("vggpr")
            elif nrow == 1:
                f.write("vggps")
            elif nrow == 2:
                f.write("cnnpr")
            else:
                f.write("cnnps")
            nrow+=1
            for i in row:
                f.write(f",{i}")
            f.write("\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pr", help="Path to the PR image")
    parser.add_argument("ps", help="Path to the PS image")
    args = parser.parse_args()
    print(f"Predict PR PS (c) {copyright.decode('utf-8')}")
    print("==============================")
    print(f"TF:{tf.__version__}")
    res = []
    res.append(load_and_predict("mv1.dll", args.pr))
    res.append(load_and_predict("mv2.dll", args.ps))
    res.append(load_and_predict("mv3.dll", args.pr, True))
    res.append(load_and_predict("mv4.dll", args.ps, True))
    to_csv(res)
    print(res)

# [array([1., 0., 0., 0., 0., 0.], dtype=float32), array([3.4461447e-13, 1.0000000e+00, 1.5850183e-19, 3.8557758e-28,
#        3.0276409e-31, 1.8420920e-28], dtype=float32), array([1.00000000e+00, 7.09595234e-18, 6.37227084e-29, 9.66254796e-22,
#        2.14474540e-20, 1.11643855e-26], dtype=float32), array([1.0000000e+00, 3.5447128e-30, 2.8260548e-33, 2.7034038e-28,
#        5.7300249e-30, 3.3122426e-35], dtype=float32)]