r,c=list(int(i) for i in input().split())
A=[]
for i in range(r):
    x=input()
    q=list(x)
    A.append(q)
dp=[[0 for j in range(c)]for i in range(r)]
for i in range(r):
    for j in range(c):
        if i>=1 and j>=1:
            if A[i][j]=="#":
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
            else:
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])
        elif i==0 and j!=0:
            if A[i][j]!="#":
                dp[i][j]=dp[i][j-1]
            else:
                dp[i][j]=dp[i][j-1]+1
        elif i!=0 and j==0:
            if A[i][j]!="#":
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+1
        else:
            if A[i][j]=="#":
                dp[i][j]=1


print(dp[-1][-1])
