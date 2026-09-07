# Basic hashing: frequency of a character in a string
def hashing(s,c):
    arr=[0]*256
    for i in s:
        arr[ord(i)]+=1
    return arr[ord(c)]

print(hashing("abcdabefc","e"))
