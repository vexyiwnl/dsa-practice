# Rotate array right by k places
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

def rotatearr(arr,k):
    n=len(arr)
    k=k%n
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    print(arr)

rotatearr([1,2,3,4,5,6,7],3)
