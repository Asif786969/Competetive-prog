n=int(input())
A=list(int(i) for i in input().split())
prefixsum=[0 for i in range(n+1)]
for i in range(1,n+1):
    prefixsum[i]=A[i-1]+prefixsum[i-1]
#print(prefixsum)
dp=[[0 for i in range(n)] for j in range(n)]
for i in range(n-1,-1,-1):
    for j in range(i,n):
        #starting index i and ending j
        #finally we need to print first row last column
        #which represent the cost of all the elements
        if i==j:
            dp[i][j]=0
        else:
            dp[i][j]=10**18
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+prefixsum[j+1]-prefixsum[i])
print(dp[0][-1])
