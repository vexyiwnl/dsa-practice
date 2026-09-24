# Majority element (> n/2 times)
'''brute force
def majority(arr):
    d={}
    for i in range(len(arr)):
        d[arr[i]]=d.get(arr[i],0)+1
    for key,value in d.items():
        if value>len(arr)//2:
            return key
'''
def majority(arr):
    count=0
    candidate=0
    for i in arr:
        if count==0:
            candidate=i
            count+=1
        elif i==candidate:
            count+=1
        else:
            count-=1
    return candidate

print(majority([3,2,3]))
print(majority([2,2,1,1,1,2,2]))
print(majority([1,1,2,3,1]))
