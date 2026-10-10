# Best time to buy and sell stock
'''def stocks(arr):
    best=0
    for buy in range(len(arr)):
        for sell in range(buy+1,len(arr)):
            best=max(best,arr[sell]-arr[buy])
    return best'''

def stocks(arr):
    best=0
    cheapest=arr[0]
    for i in range(1,len(arr)):
        cheapest=min(cheapest,arr[i])
        profit=arr[i]-cheapest
        best=max(best,profit)
    return best

print(stocks([7,1,5,3,6,4]))
print(stocks([7,6,4,3,1]))
print(stocks([5,6,1,4]))
