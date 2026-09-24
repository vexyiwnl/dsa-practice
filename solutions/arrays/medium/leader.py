# Leaders in an array
def leader(arr):
    newarr=[]
    maxsofar=float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>maxsofar:
            newarr.append(arr[i])
            maxsofar=arr[i]
    return newarr[::-1]

print(leader([1,2,5,3,1,2]))
print(leader([1,2,3,4,5]))
print(leader([5,4,3,2,1]))
print(leader([]))
