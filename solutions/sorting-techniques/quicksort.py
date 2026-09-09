# Quick sort
import random

def quicksort(arr):
    if len(arr)==1 or len(arr)==0:
        return arr
    p=arr[random.randint(0,len(arr)-1)]
    smaller=[]
    equal=[]
    greater=[]
    for i in range(len(arr)):
        if arr[i]<p:
            smaller.append(arr[i])
        elif arr[i]==p:
            equal.append(arr[i])
        else:
            greater.append(arr[i])
    smaller=quicksort(smaller)
    greater=quicksort(greater)
    return smaller+equal+greater

print(quicksort([3,3,3,3]))        # [3,3,3,3]
print(quicksort([12,9,1,4,2]))     # [1,2,4,9,12]
print(quicksort([5,1,5,2,5]))      # [1,2,5,5,5]
print(quicksort([]))               # []
