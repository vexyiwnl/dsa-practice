# Maximum subarray sum (Kadane's algorithm)
'''def maxsubarr(arr):
    best=float('-inf')
    for i in range(len(arr)):
       s=0
       for j in range(i,len(arr)):
           s+=arr[j]
           if s>best:
               best=s
    return best'''

def maxsubarr(arr):
    best=float('-inf')
    current=float('-inf')
    for i in range(len(arr)):
        extend=current+arr[i]
        fresh=arr[i]
        current = max(extend, fresh)
        best=max(current,best)
    return best

print(maxsubarr([-2,1,-3,4,-1,2,1,-5,4]))
print(maxsubarr([-3, -1, -2]))
