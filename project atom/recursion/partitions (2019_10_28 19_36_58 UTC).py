#The partitions of a no is same as a coin change problem
amt=12
coins=amt
A=[[0 for i in range(amt+1)]for j in range(amt+1)]
A[0][0]=1
#i denotes the coins
#and j denotes the values/amount
for i in range(1,amt+1):
    for j in range(0,amt+1):
        if(i>j):
            A[i][j]=A[i-1][j]
        else:
            A[i][j]=A[i-1][j]+A[i][j-i]
print(A[amt][amt])
