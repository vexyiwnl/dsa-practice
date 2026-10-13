# Set matrix zeroes
'''def matrixzeros(arr):
    rowzero=set()
    colzero=set()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==0:
                rowzero.add(i)
                colzero.add(j)
    for k in rowzero:
        for j in range(len(arr[k])):
            arr[k][j]=0
    for k in colzero:
        for i in range(len(arr)):
            arr[i][k]=0
    return arr'''

def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    col0 = False   # "column 0 must be zeroed" — kept outside the matrix

    # Pass 1: only drop flags
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0          # flag row i (column 0 = row flags)
                if j == 0:
                    col0 = True           # corner is taken, so use the boolean
                else:
                    matrix[0][j] = 0      # flag column j (row 0 = column flags)

    # Pass 2: inner cells, one at a time, reading the flags
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Pass 3: row 0, using the corner
    if matrix[0][0] == 0:
        for j in range(n):
            matrix[0][j] = 0

    # Pass 4: column 0, using col0
    if col0:
        for i in range(m):
            matrix[i][0] = 0

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[1,1,1],[0,1,1],[1,1,1]]))
