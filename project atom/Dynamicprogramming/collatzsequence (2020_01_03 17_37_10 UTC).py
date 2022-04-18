
Z=5*(10**6)+1
def calculate(i,dp):
    if(i==1):
        dp[i]=1
        return dp[i]
    else:
        if(dp[i]!=0 and i<Z):
            return dp[i]
        else:
            if(i%2==0):
                dp[i]=calculate(i//2,dp)+1
            else:
                dp[i]=calculate(3*i+1,dp)+1
            return dp[i]
dp=[0 for p in range(Z)]
i=10
print(calculate(i,dp))
print(dp.index(max(dp[0:i])))
