# Recursive bubble sort
def recbubble(arr,i=None):
    if i is None:
        i = len(arr) - 1
    if i<1:
        return arr
    check=0
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            check=1
    if check==0:
        return arr
    return recbubble(arr,i-1)

print(recbubble([12,9,1,4,2]))
print(recbubble([2,1]))
