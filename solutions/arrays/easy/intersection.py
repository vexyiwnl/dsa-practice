# Intersection of two sorted arrays
def intersection(a,b):
    arr=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            arr.append(a[i])
            i+=1
            j+=1
        elif a[i]<b[j]:
            i+=1
        else:
            j+=1
    return arr

print(intersection([1,2,2,3,3,3],[2,3,3,4,5,7]))
print(intersection([5,6],[1,5]))
