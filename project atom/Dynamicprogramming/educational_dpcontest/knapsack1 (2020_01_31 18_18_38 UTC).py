n,Capacity=list(int(i) for i in input().split())
maxv=0
W=[]
Values=[]
for i in range(n):
    w,v=list(int(i) for i in input().split())
    if v>maxv:
        maxv=v
    W.append(w)
    Values.append(v)
dp=[[0 for j in range(Capacity+1)]for i in range(n+1)]
for i in range(n+1):
    for w in range(Capacity+1):
        if i==0 or w==0:
            dp[i][w]=0
        elif w>=W[i-1]:
            dp[i][w]=max(dp[i-1][w],Values[i-1]+dp[i-1][w-W[i-1]])
        else:
            dp[i][w]=dp[i-1][w]
print(dp[-1][-1])
