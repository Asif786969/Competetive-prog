from sys import setrecursionlimit
setrecursionlimit(1000000000)
n=10000
def fib(n,dp):
    if(dp[n]!=-1):
        return dp[n]
    if n==1 or n==2:
        res=1
    else:
        res=fib(n-1,dp)+fib(n-2,dp)
    dp[n]=res
    return dp[n]
dp=[-1 for i in range(n+1)]
print(fib(n,dp))
