# Print N to 1 using recursion
def recn(n,N):
    if n<=N:
        recn(n+1,N)
        print(n)


recn(1,5)
