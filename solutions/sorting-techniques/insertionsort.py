# Insertion sort
def insertionsort(arr):
    for i in range(1,len(arr)):
        p=i-1
        val=arr[i]
        while p>=0 and val<arr[p]:
            arr[p+1]=arr[p]
            p-=1
        arr[p+1]=val
    return arr

print(insertionsort([12,9,1,4,2]))
