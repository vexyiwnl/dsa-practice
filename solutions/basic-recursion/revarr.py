# Reverse an array using recursion
def revarr(arr,l,r):
    if l>=r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    revarr(arr,l+1,r-1)

arr=[1,2,3,4,5]
revarr(arr,0,len(arr)-1)
print(arr)
