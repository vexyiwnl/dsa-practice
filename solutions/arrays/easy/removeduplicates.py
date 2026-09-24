# Remove duplicates from sorted array
def removeduplicates(arr):
    if len(arr)==0:
        return 0
    c=1
    n=len(arr)
    i=0
    while i<n-1:
        if arr[i]!=arr[i+1]:
            arr[c]=arr[i+1]
            c+=1
        i+=1
    return c

print(removeduplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeduplicates([]))
