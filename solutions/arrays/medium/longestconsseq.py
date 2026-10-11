# Longest consecutive sequence
def longestseq(arr):
    s=set(arr)
    best=0
    for i in s:
        c=1
        x=1
        if i-1 not in s:
            while i+x in s:
                c+=1
                x+=1
        best=max(best,c)
    return best

print(longestseq([100,4,200,1,3,2]))
print(longestseq([7]))
