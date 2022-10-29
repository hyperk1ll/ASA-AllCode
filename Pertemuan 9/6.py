# 6.Segitiga Siku-Siku??

def SegitigaSikuSiku(x):
    if x[0] <= 0 or x[0] <= 0 or x[0] <= 0:
        return "Inputan sisi salah"
    elif x[0] ** 2 + x[1] ** 2 == x[2] ** 2:
        return "Segitiga siku-siku"
    else:
        return "Bukan segitiga siku-siku"


x = list(map(int, input().split()))
print(SegitigaSikuSiku(x))