import sys
n,c=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
dp=[0 for i in range(n)]
delta=0
for i in range(1,n):
    x=10**13
    for j in range(1,n):
        if(i-j>=0):
            prev=x
            x=min(x,dp[i-j]+(A[i]-A[i-j])**2+c)
            if(x<prev):
                delta=i-j

    dp[i]=x
print(dp[-1])
