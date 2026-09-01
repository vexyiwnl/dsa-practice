# Prime number check
def prime(n):
    l=[]
    ql=[]
    i=1
    while i**2<=n:
        if n%i==0:
            q=n//i
            l.append(i)
            if i!=q:
                ql.append(q)
        i+=1
    l=l+ql
    return len(l)==2

print(prime(3))
