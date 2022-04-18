for _ in range(int(input())):
    n=int(input())
    B=list(int(i) for i in input().split())
    A=[]
    for i in range(n):
        x=[]
        for j in range(2):
            if j==0:
                x.append(1)
            else:
                x.append(B[i])
        A.append(x)
    dp=[[-10**12 for j in range(2)] for i in range(n)]
    #print(dp)
    for p in range(2):
        dp[0][p]=0
    for i in range(1,n):
        for j in range(2):
            for k in range(2):
                alp=abs(A[i-1][k]-A[i][j])+dp[i-1][k]
                dp[i][j]=max(dp[i][j],alp)
    print(max(dp[-1]))
