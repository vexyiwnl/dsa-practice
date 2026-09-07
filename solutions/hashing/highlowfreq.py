# Highest and lowest occurring frequencies in an array
def hashing(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return max(d.values()),min(d.values())

print(hashing([2,2,3,4,2]))
