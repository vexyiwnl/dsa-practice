# Reverse a number
n=int(input("enter number: "))
N=0
while n>0:
    r=n%10
    n=n//10
    N=N*10+r
print(N)
