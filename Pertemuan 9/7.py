# 7.Kalkulator Klasik (easy)

def KalkulatorKlasik(A, O, B):
    try:
        if O == '+':
            if A + B < -999 or A + B > 999:
                return "E"
            else:
                return A + B
        elif O == '-':
            if A - B < -999 or A - B > 999:
                return "E"
            else:
                return A - B
        elif O == '*':
            if A * B < -999 or A * B > 999:
                return "E"
            else:
                return A * B
        elif O == '/':
            if A // B < -999 or A // B > 999:
                return "E"
            else:
                return A // B
        else:
            return "Operasi tidak dikenal"

    except ZeroDivisionError:
        return "E"

A = int(input())
O = input()
B = int(input())

print(KalkulatorKlasik(A, O, B))