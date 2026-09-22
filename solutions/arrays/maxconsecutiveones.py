# Maximum consecutive ones
def maxconsones(arr):
    c=0
    r=0
    for i in range(len(arr)):
        if arr[i]==1:
            r+=1
        else:
            r=0
        c=max(r,c)
    return c

print(maxconsones([1,1,0,0,1,1,1,0]))
