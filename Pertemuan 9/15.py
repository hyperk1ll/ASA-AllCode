# 15.Hari Kebalikan

def reverseString(str):
    out = ""
    
    for i in range(len(str)):
        out += str[len(str) -i - 1]
    
    return out

str = input()

print(reverseString(str))