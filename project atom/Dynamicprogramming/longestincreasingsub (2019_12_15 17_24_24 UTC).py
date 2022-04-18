#THE # QUESTION: IS TO FIND THE MAXIXIMUM ACHEIVABLE INCREASUNG LENGTH OF AN ARRAY BY REMOVING AN ELEMENT
#n=int(input())
#A=list(int(i) for i in input().split())

A=[1,2,0,4,0,6,8,1,2]
n=len(A)
print(n)
dp=[1 for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if(A[i]>A[j] and dp[j]+1>dp[i]):
            dp[i]=dp[j]+1
        else:
            dp[i]=dp[i-1]
print(dp)
