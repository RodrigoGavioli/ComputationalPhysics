def Catalan():
    LNumber = []
    C = 1
    n = 0
    while C < 10**9:
        n += 1
        LNumber.append(C)
        C *= ((4*n + 2)/(n+2))
    return LNumber

print(Catalan())