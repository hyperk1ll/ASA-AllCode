# 17.PlustoMin, MintoPlus!

def plustoMin(x):
    return [-i for i in x]



x = int(input())
a = list(map(int, input().split()))[:x]

print(plustoMin(a))