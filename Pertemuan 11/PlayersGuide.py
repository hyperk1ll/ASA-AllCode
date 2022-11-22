def value(harga, power, gold, N):
    N = len(power)

    X = [[0 for x in range(gold + 1)] for x in range(N + 1)]
    i = 0

    for i in range(N + 1):
        for gold in range(gold + 1):
            if gold == 0 or i == 0:
                X[i][gold] = 0
            elif harga[i-1] > gold: 
                X[i][gold] = X[i-1][gold]
            else:
                X[i][gold] = max(power[i - 1] + X[i - 1][gold - harga[i - 1]], X[i - 1][gold])
    return X[N][gold]

harga = []
power = []
N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    harga.append(a)
    power.append(b)
gold = int(input())

print(value(harga, power, gold, N))