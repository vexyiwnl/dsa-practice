# Longest subarray with sum k
'''def longestsubarray(arr,k):
    best=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]
            if s==k and (j+1)-i>best:
               best=(j+1)-i
    return best'''

def longestsubarray(arr,k):
    p={0: -1}
    s=0
    best=0
    for j in range(len(arr)):
        s+=arr[j]
        if s-k in p:
            length=j-p[s-k]
            best=max(best,length)
        if s not in p:
            p[s]=j
    return best

print(longestsubarray([10,5,2,7,1,-10], k=15))
print(longestsubarray([0,0,5], k=5))
print(longestsubarray([10,5,2,7,1,-10], k=15))
