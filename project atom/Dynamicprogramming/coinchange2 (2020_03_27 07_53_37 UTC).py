def coinchange(A,dp,Sum):
    dp[0]=1
    for coin in A:
        for i in range(1,len(dp)):
            if(i>=coin):
                dp[i]+=dp[i-coin]
    return dp[Sum]


#Sum,N=list(int(i) for i in input().split(" "))
#A=list(int(i) for i in input().split(" "))
Sum=4
A=[1,2]
dp=[0 for i in range(Sum+1)]
print(coinchange(A,dp,Sum))
