# 3.N-rotasi Array

from collections import deque

def NRotateArr(nums, n):
    x = deque(nums)
    x.rotate(n - 1)

    # return list(x)

    s = [str(i) for i in list(x)]

    res = " ".join(s)

    return res

nums = list(map(int, input().split()))
n = int(input())

print(NRotateArr(nums, n))