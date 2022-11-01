# 16.Kata yang disensor

def sensorKata(x, y):
    j = 0

    for i in range(0, len(x)):
        if x[i] == "*":
            x[i] = y[j]
            j += 1
    
    return ''.join(x)

x = list(input())
y = input()

print(sensorKata(x, y))