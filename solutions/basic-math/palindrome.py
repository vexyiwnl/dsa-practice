# Palindrome number check
n1=int(input("enter number: "))
n=n1
n2=0
while n>0:
    r=n%10
    n=n//10
    n2=n2*10+r

if n1-n2==0:
    print("palindrome")
else:
    print("not a palindrome")
