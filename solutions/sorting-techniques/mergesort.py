# Merge sort
def merge(arrleft,arrright):
    arrnew=[]
    i=0
    j=0
    while i<len(arrleft) and j<len(arrright):
        if arrleft[i]<arrright[j]:
            arrnew.append(arrleft[i])
            i+=1
        else:
            arrnew.append(arrright[j])
            j+=1
    arrleft=arrleft[i:]
    arrright=arrright[j:]
    arrnew.extend(arrleft)
    arrnew.extend(arrright)
    return arrnew

def mergesort(arr):
    if len(arr)==1 or len(arr)==0:
        return arr
    arrleft=arr[:(len(arr)+1)//2]
    arrright=arr[(len(arr)+1)//2:]
    arrleft=mergesort(arrleft)
    arrright=mergesort(arrright)
    return merge(arrleft,arrright)

print(mergesort([12,9,1,4,2]))   # [1, 2, 4, 9, 12]
print(mergesort([]))             # []
print(mergesort([5]))            # [5]
print(mergesort([2,1]))          # [1, 2]
