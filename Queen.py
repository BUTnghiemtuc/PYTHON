n = 0
cot = []
xuoi = []
nguoc = []
a = []

def inCauHinh(): 
    for i in range(1, n + 1): 
        for j in range(1, n + 1): 
            if a[i] == j: 
                print('#', end = " ")
            else: 
                print('.', end = " ")
        print()

def Try(i): 
    for j in range(1, n + 1): 
        if not cot[j] and not xuoi[i - j + n] and not nguoc[i + j - 1]: 
            a[i] = j
            cot[j] = xuoi[i - j + n] = nguoc[i + j - 1] = True
            if i == n: 
                inCauHinh()
                print()  # Print a new line after each configuration
            else: 
                Try(i + 1)
            cot[j] = xuoi[i - j + n] = nguoc[i + j - 1] = False

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    cot = [False] * (n + 1)
    xuoi = [False] * (2 * n + 1)
    nguoc = [False] * (2 * n + 1)
    a = [0] * (n + 1)
    Try(1)
