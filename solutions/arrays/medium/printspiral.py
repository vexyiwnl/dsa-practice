# Spiral order traversal of a matrix
def spiral(arr):
    top=0
    bottom=len(arr)-1
    left=0
    right=len(arr[0])-1
    res=[]
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            res.append(arr[top][i])
        top+=1
        for j in range(top,bottom+1):
            res.append(arr[j][right])
        right-=1
        if top<=bottom:
            for k in range(right,left-1,-1):
                res.append(arr[bottom][k])
            bottom-=1
        if left<=right:
            for m in range(bottom,top-1,-1):
                res.append(arr[m][left])
            left+=1
    return res

print(spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
