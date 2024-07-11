from math import *

def Binpow(a, b): 
    res = 1
    while b != 0: 
        if b % 2 == 1: 
            res = res * a
        a = a * a
        b //= 2
    return res 

def binpow(a, b): 
    if b == 0: 
        return 1
    res = binpow(a, b // 2) 
    if b % 2 == 1:  
        return res * res * a 
    return res * res

if __name__ == '__main__':
    # a, b = map(int, input().split())
    # print(binpow(a, b))

    t = list(range(1, 6)) # tao ra 1 list [1, 2, 3, 4, 5]
    for it in t: 
        print(it, end=' ')

# Cắt List a[start : stop : step]

    a = t[2:]
    print(a)
    b = t[::-1] # reverse
    print(b, t)

