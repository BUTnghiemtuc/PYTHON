from math import *

for i in range(1, 10, 1):
    print(i, 'Hello', end = " ")
    
print()
print("Im better")

for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1): 
        print("*", end="")
    print()

def Chao(ten):
    print(f"Minh ten la: {ten}")

str = "Khoi Thieu Lam Chu"
str1 = str.split()
for s in str1:
    Chao(s)

val = (1, 2, 3, 4, 5)
a = list(val)
print(a)