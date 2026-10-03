# Two sum
def twosum(arr,target):
    d={}
    for i in range(len(arr)):
        if target-arr[i] in d:
            return (d[target-arr[i]],i)
        d[arr[i]]=i
    return None

print(twosum([3,2,4],6))
print(twosum([2,7,11,3],9))
