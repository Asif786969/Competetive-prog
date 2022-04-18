import sys
n,c=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
dp=[0 for i in range(n)]
for i in range(1,n):
    x=10**13
    for j in range(1,n):
        if(i-j>=0):
            x=min(x,dp[i-j]+(A[i]-A[i-j])**2+c)
    dp[i]=x
print(dp[-1])
