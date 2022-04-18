#THE # QUESTION: IS TO FIND THE MAXIXIMUM ACHEIVABLE INCREASUNG LENGTH OF AN ARRAY BY REMOVING AN ELEMENT
#n=int(input())
#A=list(int(i) for i in input().split())

A=[1,2,0,4,0,6,7,8,9,-1,2,3,7,8]
n=len(A)
dp=[1 for i in range(n+1)]
for i in range(1,n):
    if(A[i]>A[dp[i-1]-1]):
        dp[i]=dp[i-1]+1
    else:
        dp[i]=dp[i-1]
print(dp[n])
