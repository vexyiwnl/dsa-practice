# Rearrange array elements by sign
def rearrange(arr):
    res=[0]*len(arr)
    p=0
    n=1
    for i in arr:
        if i>0:
            res[p]=i
            p+=2
        else:
            res[n]=i
            n+=2
    return res

print(rearrange([3,1,-2,-5,2,-4]))
print(rearrange([-1,1]))
