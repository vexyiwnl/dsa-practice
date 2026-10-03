# Sort an array of 0s, 1s and 2s
'''def sort012(arr):
    c0=0
    c1=0
    c2=0
    for i in range(len(arr)):
        if arr[i]==0:
            c0+=1
        elif arr[i]==1:
            c1+=1
        else:
            c2+=1
    for j in range(len(arr)):
        if j<c0:
            arr[j]=0
        elif j<c0+c1:
            arr[j]=1
        else:
            arr[j]=2
    return arr'''

def sort012(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr

print(sort012([2,0,2,1,1,0]))
print(sort012([2,0,1]))
print(sort012([0]))
print(sort012([1,2,0]))
