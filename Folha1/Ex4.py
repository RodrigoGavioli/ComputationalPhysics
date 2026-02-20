import numpy as np
def Potencial(L):
    L = int(L)
    sum = 0
    for i in range(-L,L):
        for j in range(-L,L):
            for k in range(-L,L):

                sum += 1/np.sqrt(i**2+j**2+k**2)
    return sum

def potencial(i,j,k,sum):
    if i == 0 and j == 0 and k == 0:
        return 0
    pot = 1/np.sqrt(i**2+j**2+k**2)
    if (i+j+k) %2 == 0:
        sum += pot
        return sum + potencial(i+1,j,k,sum) + potencial(i,j+1,k,sum) + potencial(i,j,k+1,sum)
    else:
        sum -= pot
        return sum + potencial(i+1,j+1,k+1,sum) + potencial(i,j+1,k,sum) + potencial(i,j,k+1,sum)
    
def Calculo(L):
    return potencial(-L,-L,-L,0)

print(Calculo(10))

