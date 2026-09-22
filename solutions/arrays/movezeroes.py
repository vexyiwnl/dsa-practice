# Move zeroes to end of array
'''
def movezeroes(arr):
    n=len(arr)
    w=0
    for r in range(n):
        if arr[r]!=0:
            arr[w]=arr[r]
            w+=1
    for i in range(w,n):
        arr[i]=0
    return arr
'''
def movezeroes(arr):
    n=len(arr)
    w=0
    for r in range(n):
        if arr[r]!=0:
            arr[w],arr[r]=arr[r],arr[w]
            w+=1
    return arr

print(movezeroes([0,1,0,3,12]))
