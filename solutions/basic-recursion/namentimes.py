# Print name N times using recursion
def name(n,N):
    if n!=N:
        print("name")
        return name(n+1,N)

name(0,3)
