# 9.Ketentuan ToRa

def KetentuanToRa(x):
    return round(sum(x) / len(x), 2)

n = int(input())
x = list(map(int, input().split()))[:n]

print(KetentuanToRa(x))
print(KetentuanToRa(x) * 2)