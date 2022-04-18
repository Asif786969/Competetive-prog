#THE # QUESTION: IS TO FIND THE MAXIXIMUM ACHEIVABLE INCREASUNG LENGTH OF AN ARRAY BY REMOVING AN ELEMENT
#n=int(input())
#A=list(int(i) for i in input().split())

A=[ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
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
