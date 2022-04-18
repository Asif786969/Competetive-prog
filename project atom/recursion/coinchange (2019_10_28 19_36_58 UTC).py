coins=[1,3,5,7]
amt=8
dp=[[1 for i in range(amt+1)] for j in range(len(coins))]
for i in range(1,len(coins)+1):
    for j in range(amt+1):
        if(coins[i]>j):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
print(dp[len(coins)][amt])
