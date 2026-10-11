# Replace elements with greatest element on right side
'''def replaceelements(arr):
    newarr=[-1]*len(arr)
    for i in range(1,len(arr)):
        maxsofar=max(arr[i:])
        newarr[i-1]=maxsofar
    return newarr'''

def replaceelements(arr):
    maxele=-1
    for i in range(len(arr)-1,-1,-1):
        temp=arr[i]
        arr[i]=maxele
        if temp>maxele:
            maxele=temp
    return arr

print(replaceelements([17,18,5,4,6,1]))
