# Largest element in an array
def largest(arr):
    if len(arr)==0:
        return None
    sol=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>sol:
            sol=arr[i]
    return sol

print(largest([-4,-6,-2,-8]))
