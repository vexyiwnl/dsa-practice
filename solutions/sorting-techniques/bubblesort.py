# Bubble sort
def bubblesort(arr):
    for i in range((len(arr)-1),0,-1):
        check=0
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                check=1
        if check==0:
            break
    return arr

print(bubblesort([2,1]))
