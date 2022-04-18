#A=list(int(i) for i in input().split())
A=[2,3,1,1,2,4,2,0,1,1]
L=len(A)
dp=[0 for i in range(L)]
for i in range(1,L):
    ans=10000
    for j in range(i-1,-1,-1):
        if (A[j]+j)>=i:
            ans=min(ans,dp[j]+1)
    dp[i]=ans
print(*dp)
