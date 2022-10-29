# 8.Persamaan Kuadrat

def PersamaanKuadrat(list, x):
    return list[0] * (x ** 2) + (list[1] * x) + list[2]
        
list = list(map(int, input().split()))
x = int(input())

print(PersamaanKuadrat(list, x))