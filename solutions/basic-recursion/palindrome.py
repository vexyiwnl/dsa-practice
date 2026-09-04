# Check if a string is a palindrome using recursion
def ispal(s,l,r):
    if l>=r:
        return True
    return s[l] == s[r] and ispal(s, l+1, r-1)

s="madam"
print(ispal(s,0,len(s)-1))
