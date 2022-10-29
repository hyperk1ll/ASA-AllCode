# 11.Remed Ga Ya?

def RemedGaYa(nilai):
    if nilai >= 80 and nilai <=100:
        return "Sangat Aman"
    elif nilai >= 70 and nilai <= 79:
        return "Aman"
    elif (nilai >= 60 and nilai <= 69):
        return "Lebih Baik Remed"
    elif (nilai >= 0 and nilai <= 59):
        return "Harus Remed"
    else:
        return "Input Invalid"
    
nilai = int(input())

print(RemedGaYa(nilai))