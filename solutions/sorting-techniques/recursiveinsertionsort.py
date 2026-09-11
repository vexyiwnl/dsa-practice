# Recursive insertion sort
def recinsertion(arr,i=1):
    if i>=len(arr):
        return arr
    p=i-1
    val=arr[i]
    while p>=0 and val<arr[p]:
        arr[p+1]=arr[p]
        p-=1
    arr[p+1]=val
    return recinsertion(arr,i+1)

print(recinsertion([12,9,1,4,2]))   # [1, 2, 4, 9, 12]
print(recinsertion([]))             # []
print(recinsertion([5]))            # [5]
