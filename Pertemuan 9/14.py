# 14.PRIMA adalah Segalanya

def Bilprima(x):
    if x == 1:
        return False
    for i in range(2,x+1):
        if x % i == 0:
            if x == i:
                return True
            else:
                return False

def prima(x, y):
    a = [["O" if Bilprima(i + j) == True else "X" for j in range(1, x + 1)] for i in range(1, y + 1)]

    return a

m, n = map(int, input().split())

print(prima(m, n))