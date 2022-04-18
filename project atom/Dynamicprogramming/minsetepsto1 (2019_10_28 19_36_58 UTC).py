import sys
from sys import setrecursionlimit
setrecursionlimit(3000000)
#memoization
def minStepsTo1DP(n,dp):
    if(n==1):
        return 0
    if(dp[n-1]==-1):
        ans1=minStepsTo1DP(n-1,dp)
        dp[n-1]=ans1
    else:
        ans1=dp[n-1]

    if(n%2==0):
        if(dp[n//2]==-1):
            ans2=minStepsTo1DP(n/2,dp)
            dp[n//2]=ans2
        else:
            ans2=dp[n//2]
    else:
        ans2=sys.maxsize
    if(n%3==0):
        if(dp[n//3]==-1):
            ans3=minStepsTo1DP(n/3,dp)
            dp[n//3]=ans3
        else:
            ans3=dp[n//3]
    else:
        ans3=sys.maxsize
    ans=1+min(ans1,ans2,ans3)
    return ans
#n=int(input())
n=9
dp=[-1 for i in range(n)]
print(minStepsTo1DP(n,dp))
