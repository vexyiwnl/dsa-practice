# Union of two sorted arrays
def add(arr,val):
    if not arr or arr[-1]!=val:
        arr.append(val)

def union(a,b):
    i=0
    j=0
    arr=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            val=a[i]
            i+=1
        elif a[i]>b[j]:
            val=b[j]
            j+=1
        else:
            val=a[i]
            i+=1
            j+=1
        add(arr,val)
    for k in range(i,len(a)):
        add(arr,a[k])
    for k in range(j,len(b)):
        add(arr,b[k])
    return arr

print(union([3,4,6,7,9,9],[1,5,7,8,8]))
print(union([2,2],[2,2]))
print(union([1],[2,2,2]))
