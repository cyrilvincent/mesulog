import matplotlib.pyplot as plt
import numpy as np

nbcat = 5
f = lambda x : -1/(x-1)-1/(1-1/nbcat)
x = np.linspace(0,1,100)
y = f(x)
print(y)
plt.plot(x,y)
plt.show()

softmax = lambda x : np.exp(x)/sum(np.exp(x))
linsm = lambda x : x/sum(x)
geosm = lambda x : x**2/sum(x**2)

rvalues = np.array([0.84, 0.91, 0.92, 0.94])
print(f(rvalues))
sm = softmax(f(rvalues))
print((sm * 100).astype(int))
print(sum(sm))
sm = linsm(f(rvalues))
print((sm * 100).astype(int))
print(sum(sm))
sm = geosm(f(rvalues))
print((sm * 100).astype(int))
print(sum(sm))

# PR + PS | SVM | Max              |
# PR + PS | RF  | Max              |
# PR + PS | CNN | Dense | Softmax  |
# PR + PS | RNNs | Dense | Softmax |
# PS | CNN | LSTM | Softmax        | fdistribution(rvalues) | fnormalisation
# PR + PS | CNN | SVM | Max        | asymptotique             softmax ou geo ou linear
# PR + PS | CNN | RF | Max         |
# PR + PS | RNNs | SVM | Max       |
# PR + PS | RNNs | RF | Max        |
#
# RNNs de type XCeption et/ou Resnet

# 1 : Exe python ou C#
# 2 : Crypt
# 3 : PDF
# 4 : New models + sklearn + Transfert Learning
# 5 : Word
# 6 : GAN
