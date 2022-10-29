# 10.No Duplicate!

def NoDuplicate(a):
    x = []

    for i in a:
        if i not in x:
            x.append(i)
    return x

x = int(input())
a = list(map(int, input().split()))[:x]

print(NoDuplicate(a))