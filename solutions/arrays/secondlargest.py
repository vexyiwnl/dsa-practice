# Second largest element in an array
def seclargest(arr):
    if len(arr)<=1:
        return None
    largest=arr[0]
    sec=float('-inf')
    for i in range(1,len(arr)):
        if arr[i]>largest:
            sec=largest
            largest=arr[i]
        elif arr[i]>sec and arr[i]!=largest:
            sec=arr[i]
    if sec==float('-inf'): return None
    return sec

print(seclargest([12,9,1,4,2]))
print(seclargest([5,5,5]))
print(seclargest([5,5,3]))
print(seclargest([7]))
