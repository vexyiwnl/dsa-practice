# Rotate matrix by 90 degrees
'''def rotate(arr):
    m=len(arr)
    n=len(arr[0])
    matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[j][m-i-1]=arr[i][j]
    for i in range(m):
        for j in range(n):
            arr[i][j]=matrix[i][j]'''
def reverse(arr,start,stop):
    while start<stop:
        arr[start],arr[stop]=arr[stop],arr[start]
        start+=1
        stop-=1
    return arr

def rotate(arr):
    m=len(arr)
    n=len(arr[0])
    for i in range(m):
        for j in range(i+1,n):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(m):
        reverse(arr[i],0,m-1)
    return arr

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
