def CatalanRecursivo(n):
    if n == 0: 
        return 1
    else:
        return ((4*n-2)/(n+1))*CatalanRecursivo(n-1)
    


print(CatalanRecursivo(100))
    