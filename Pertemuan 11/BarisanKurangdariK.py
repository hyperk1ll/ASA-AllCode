list1 = []

c = 0

def barisank(num = 0, N = 0):
    global c
    hasil = 1
    if num != N:
        list1.append(L[num])
        barisank(num + 1, N)
        list1.pop()
        barisank(num + 1, N)
    
    else: #num == N
        for i in range(len(list1)):
            hasil *= list1[i]
        if K >= hasil > 0:
            c += 1
        return 
        

N = int(input())
L = list(map(int, input().split()))
K = int(input())
    
barisank(0, N)
print(c - 1)