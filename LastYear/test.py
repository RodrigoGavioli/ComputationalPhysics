import matplotlib.pyplot as plt

def count_if(xs, a, b):
    count = 0
    for i in range(len(xs)):
        if xs[i] != a and xs[i] % b != 0:
            count += 1
    return count


print(count_if([4,7,1,1], 4,7))


def sum_mult_cond(j,k,n):
    count = 0
    for i in range(1,n+1):
        if i%j == 0 or i%k ==0:
            count += i

    return count
print(sum_mult_cond(3,2,8))


def f(n):
    lista = []
    for i in range(n+1):
        lista.append(float(i/2))

    return lista
print(f(7))

def a_to_b_neg(a,b,k):
    list = []
    if k < 0:
        for i in range(a,b-1,k):
            list.append(i)
    if k > 0:
        for i in range(a, b+1,k):
            list.append(i)
    return list
print(a_to_b_neg(9,5,-2))


S = "vou comer"
print("len:", len(S))
print(S + " bolo")
print("\\")
def remove_cpp_com(txt):
    S = ""
    for i in range(len(txt)):
        if  txt[i] == "/" and txt[i+1] == "/":
            break
        S += txt[i]
    return S
print(remove_cpp_com("int main(void) {} // main function"))


def my_format(a,x):
    A =''
    pI = int((5 - (len(a)/2)))
    i = 0
    while(i<10):
        
        if i < pI:
            A += "="
            i += 1
        elif(i<len(a) and i>=pI):
            
            A += a
            i += len(a)
            
        elif(i>len(a)):
            A += "="
            i += 1
    
    return f"o valor de {A} arrendondado com 3 casas decimais é {x:.3f}"

print(my_format("hours", 14.7))
print(my_format("minutos", 3.8))