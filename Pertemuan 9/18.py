# 18.tuCar Khar

def tucarKhar(S, x, y):
    a = [i for i in S]
    a[x - 1], a[y - 1] = a[y - 1], a[x - 1]
    
    return ''.join(a)

x = input()
i, j = map(int, input().split())

print(tucarKhar(x, i, j))
