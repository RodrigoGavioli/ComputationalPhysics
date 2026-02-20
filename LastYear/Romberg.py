import numpy as np
def f(x):
    return x**2

a = 0
b = 2
integral = np.array([])
R = np.array([])
n = np.array([1,2,4,8,16,32])
print(n)

for i in range(len(n)):
    s = 0
    h = (b-a)/n[i]
    s = (f(a) + f(b))*0.5
    for k in range(1,int(n[i])):
        s += f(a+k*h)
    integral = np.append(integral,[s*h])

for j in range(1, len(integral)):
  
    r = integral[j] + (1/3)*(integral[j]-integral[j-1])
    R = np.append(R, [r])



print(R)