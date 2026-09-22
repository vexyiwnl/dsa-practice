# Linear search
def linearsearch(arr,t):
    for i in range(len(arr)):
        if arr[i] == t:
            return i
    return -1

print(linearsearch([2,3,4,5,3],3))
