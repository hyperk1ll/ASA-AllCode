# 20. Mencocokkan Pattern (Brute Force)

def bruteForce(s1, s2):
    x = len(s1)
    y = len(s2)
    
    if y > x:
        return "\nPattern tidak ditemukan"
    else:
        Found = False
        for i in range(0, x):
            print(s1[i:i + y])
            j = 0
            while j < y and s1[i] == s2[j]:
                i = i + 1
                j = j + 1
            if j == y:
                Found = True
                return "\nPattern ditemukan"
        if not Found:		
            return "\nPattern tidak ditemukan"

"""
def bruteForce(*, text, pattern):

    n, m = len(text), len(pattern)
    for i in range(1 + (n - m)):
        match = True
        for j in range(m):
            print(text[i:i+m])
            if text[i + j] != pattern[j]:
                match = False
                break
        
        if match:
            return "\nPattern ditemukan!!"
    if not match:
        return "\nPattern tidak ditemukan!!"
"""

"""
def bruteForce(s1, s2):
    i = 0
    j = 0

    while i < len(s1) and j < len(s2):
        # print(s1[i:len(s2) + i])
        if s1[i] != s2[j]:
            i = i - j + 1
            j = 0
            
        elif s1[i] == s2[j]:
            i = i + 1
            j = j + 1

            
    if(j >= len(s2)):
        return "\nPattern ditemukan!!"
        
    else:
        return "\nPattern tidak ditemukan!!"
"""


a = input()
b = input()

print(bruteForce(a, b))