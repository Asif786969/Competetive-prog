l=10
Lengths=[2,3]
Costs=[4,3]
dp=[0 for i in range(l+1)]
for i in range(1,l+1):
    cost=10**2+1
    for j in range(len(Lengths)):
        if i>=Lengths[j]:
            cost=min(dp[i-Lengths[j]]+Costs[j],cost)
        if cost!=10**2+1:
            dp[i]=cost
print(dp)
