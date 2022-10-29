# 1.Hitung Karakter

def HitungKarakter(str, n):
    x = (str * (n // len(str) + 1))[:n]
    return x.count('A')

str = input()
n = int(input())