# Count digits of a number
#normal method O(log n)
'''
n=int(input("enter a number: "))
n=abs(n)
q=n//10
c=1

while q>0:
    q=q//10
    c+=1

print(c)
'''

#log method
import math
n=int(input("enter number: "))
d=math.log(n,10)
print(f"number of digits: {math.trunc(d)+1}")
