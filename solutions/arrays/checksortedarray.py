# Check if array is sorted and rotated
def checksort(arr):
    c=0
    for j in range(len(arr)):
        if arr[j]>arr[(j+1)%len(arr)]:
            c+=1
    return c<=1

print(checksort([1,2,3]))
print(checksort([3,4,5,1,9]))
print(checksort([2,1]))
print(checksort([1,5,2,4]))
print(checksort([5,5,5]))
print(checksort([3,3,1,3]))
