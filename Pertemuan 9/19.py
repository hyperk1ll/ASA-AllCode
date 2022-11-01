# 19.Banyaknya Langkah (Rekursif)

def banyakLangkah(x):
    if x > 0:
        return x
    else:
        return x * banyakLangkah(x - 1)

x = int(input())

print(banyakLangkah(x))