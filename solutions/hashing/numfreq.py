# Basic hashing: frequency of a number in an array
def hashing(arr,n):
    newarr=[0]*(max(arr)+1)
    for i in arr:
        newarr[i]+=1
    return newarr[n]

print(hashing([2,2,3,4,2],2))
