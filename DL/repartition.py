import matplotlib.pyplot as plt
import numpy as np

# f repartition
nbcat = 6
f = lambda x : -1/(x-1)-1/(1-1/nbcat)
x = np.linspace(0,1,100)
y = f(x)
print(y)
plt.plot(x,y)
#plt.show()

# f normalisation
softmax = lambda x : np.exp(x)/sum(np.exp(x))
linsm = lambda x : x/sum(x)
geosm = lambda x : x**2/sum(x**2)

rvalues = np.array([0.8,0.89,0.79,0.75]) #,0.59,0.69]) #Deterministe, CNN PR, CNN PS, VGG PR, VGG PS
print("Asymptote",f(rvalues))
sm = softmax(f(rvalues))
print("Softmax",np.round(sm * 100).astype(int))
print(sum(sm))
sm = linsm(f(rvalues))
print("Linear",np.round(sm * 100).astype(int))
print(sum(sm))
sm = geosm(f(rvalues))
print("Geo",np.round(sm * 100).astype(int))
print(sum(sm))

