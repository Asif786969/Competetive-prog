n,c=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
dp=[0 for i in range(n+1)]
for i in range(1,n):
    cost=10**19
    for j in range(i):
        cost=min(cost,dp[j]+(A[i]-A[j])**2+c)
        print(dp[j]+(A[i]-A[j])**2+c,end=" ")
    dp[i]=cost
    print()
print(dp)
