# 5.Adu Panco
import math

def AduPanco(A, x): 
    i = 0

    while i < len(x):
        while A > x[i]:
            A = A = A + (math.floor(x[i]) // 2)
            i = i + 1

            if A < x[i]:
                return (f"A Kalah, penantang {i + 1} Menang\n"
                        f"Kekuatan A : {A}")

            else:
                return ("A Menang!!!\n"
                        f"Kekuatan A : {A}")
        
        return 


a = int(input())
n = int(input())
nums = list(map(int, input().split()))[:n]

print(AduPanco(a, nums))