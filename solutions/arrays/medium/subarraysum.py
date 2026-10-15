# Count subarrays with sum k
'''def subarrsum(arr,k):
    c=0
    for i in range(len(arr)):
        if arr[i]==k:
            c+=1
        s=arr[i]
        for j in range(i+1,len(arr)):
            s+=arr[j]
            if s==k:
                c+=1
    return c'''

def subarrsum(arr,k):
    p=0
    d={0:1}
    c=0
    for i in range(len(arr)):
        p+=arr[i]
        if p-k in d:
            c+=d[p-k]
        d[p]=d.get(p,0)+1
    return c

print(subarrsum([1,2,3],3))
