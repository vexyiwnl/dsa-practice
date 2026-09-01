# Armstrong number check
def armstrong(n):
    s=0
    cn=n
    c=0
    while cn>0:
        cn=cn//10
        c+=1
    n1=n
    while n1>0:
        r=n1%10
        s=s+(r**c)
        n1=n1//10
    return n==s

print(armstrong(-5))
