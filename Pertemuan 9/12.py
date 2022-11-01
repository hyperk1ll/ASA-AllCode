# 12.Tahan, Lagi Puasa!

def Puasa(x):
    if 24 >= x >= 1:
        if 18 > x > 4:
            print("TIDAK, MEMAKAN")
        elif 24 >= x >= 19:
            print("MEMAKAN, AMAN")
        elif x == 18:
            print("MEMAKAN, BERBUKA")
        else:
            print("MEMAKAN, SAHUR")

x = int(input())

print(Puasa(x))