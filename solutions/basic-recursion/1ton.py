# Print 1 to N using recursion
def recn(n,N):
    if n<=N:
        print(n)
        return recn(n+1,N)

recn(1,5)
