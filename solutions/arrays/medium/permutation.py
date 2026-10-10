# Next permutation
def reverse(arr,start,stop):
    while start<stop:
        arr[start],arr[stop]=arr[stop],arr[start]
        start+=1
        stop-=1
    return arr

def permutation(arr):
    i=len(arr)-2
    while i>=0:
        if arr[i]<arr[i+1]:
            break
        i-=1
    if i<0:
        return reverse(arr,0,len(arr)-1)
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            si=j
    arr[i],arr[si]=arr[si],arr[i]
    return reverse(arr,i+1,len(arr)-1)

print(permutation([1,3,5,4,2]))
print(permutation([3,1,4,3]))
print(permutation([3,2,1]))
print(permutation([1,3,2]))
