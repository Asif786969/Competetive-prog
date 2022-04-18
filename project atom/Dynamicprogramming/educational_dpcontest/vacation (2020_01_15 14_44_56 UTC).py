A=[]
n=int(input())
for i in range(n):
    B=list(int(j) for j in input().split())
    A.append(B)
dp=[[0 for i in range(3)]for k in range(n)]
#print(dp)
for i in range(n):
    for j in range(3):
        if i>0 and j==1:
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j+1])+A[i][j]
        elif i==0:
            dp[i][j]=A[i][j]
        elif j==0:
            dp[i][j]=max(dp[i-1][j+1],dp[i-1][j+2])+A[i][j]
        elif j==2:
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j-2])+A[i][j]
print(max(dp[-1]))
