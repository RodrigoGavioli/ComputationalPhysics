import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)


N = 10
a = 0.0
b = np.linspace(0,0.3,300)
integralsimp = np.array([])


for i in range(len(b)):
    h = (b[i]-a)/N
    s = f(a) + f(b[i])
    for k in range(1, N, 2):
        s += 4*(f(a+k*h))
    for j in range(2, N, 2):
        s += 2*(f(a+j*h))
    s = (h/3)*(s)
    integralsimp = np.append(integralsimp,[s])
print(integralsimp)

plt.plot(integralsimp)
plt.show()


