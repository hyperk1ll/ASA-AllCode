# 4.Perkalian Matriks dan Bilangan

def KaliMatrix(a, matrix):
    return [[j * a for j in i] for i in matrix]

a = int(input())
m, n = map(int, input().split())

x = [[int(j) for j in input().split()] for i in range(m)]

print(KaliMatrix(a, x))
