import sys,math
def minsquares(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    for i in range(1,n+1):
        root=int(math.sqrt(i))
        ans=sys.maxsize
        for j in range(1,root+1):
            curr=1+dp[i-(j**2)]
            ans=min(ans,curr)
        dp[i]=ans
    return dp[n]


#n=int(input())
n=19
print(minsquares(n))
