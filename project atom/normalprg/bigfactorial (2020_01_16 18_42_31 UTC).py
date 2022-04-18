import sys
sys.setrecursionlimit(10000)
p=10**9+7
def fact(a):
    ans=1
    while(a!=0):
        ans*=a
        a-=1
    return ans
def calculate(x,m):
    if m==0 or x==m:
        return 1
    return calculate(x-1,m-1)+calculate(x-1,m)
def dpwe(n,r):
    dp=[[1 for i in range(n+1)]for j in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
    print(dp)

n=4
r=2
#print(calculate(n,r))
dpwe(n,r)
#print((fact(n)//(fact(r)*fact(n-r)))%p)
