# Find the missing number in an array
def findmissing(arr):
    n=len(arr)
    a=(n*(n+1))//2
    b=sum(arr)
    return a-b

print(findmissing([3,0,1]))
