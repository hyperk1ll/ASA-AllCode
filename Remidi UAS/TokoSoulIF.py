def findMin(V, arr):
    n = len(arr)
     
    ans = []
 
    i = n - 1
    while(i >= 0):
        while (V >= arr[i]):
            V -= arr[i]
            ans.append(arr[i])
 
        i -= 1
 
    return len(ans)

N, P = map(int, input().split())
arr = list(map(int, input().split()))[:N]
print(findMin(P, arr))