# 2.Mencari Pasangan

def MencariPasangan(nums, total):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == total:
                return f"{i} {j}"
    return []


nums = list(map(int, input().split()))
total = int(input())

print(MencariPasangan(nums, total))