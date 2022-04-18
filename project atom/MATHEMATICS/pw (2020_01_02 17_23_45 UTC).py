def calculate(i,dp):
    if(i==1):
        dp[i]=1
        return dp[i]
    else:
        if(dp[i]!=0):
            return dp[i]
        else:
            if(i%2==0):
                dp[i]=calculate(i//2,dp)+1
            else:
                dp[i]=calculate(3*i+1,dp)+1
            return dp[i]
dp=[0 for p in range(10**8)]
i=10
ans=calculate(i,dp)
A=dp[0:i]
print(ans)
print(A)
print(A.index(max(A)))
