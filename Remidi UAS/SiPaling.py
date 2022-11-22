n = int(input())
arr = list(map(int, input().split()))[:n]

arr.sort()

print(arr[-1])
print(arr[0])