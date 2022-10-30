# 13.Number 13

def Number13(x, y):
    a = []
    
    for i in x:
        if i - y == 13 or i - y == -13 or i + y == 13 or i + y == -13:
            a.append(i)
        else:
            a.append(y)

    return a[::-1]

a = int(input())
b = list(map(int, input().split()))[:a]
c = int(input())

print(Number13(b, c))