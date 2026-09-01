# Print all divisors of a number
def divisor(n):
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
    return l+ql[::-1]

print(divisor(8))
