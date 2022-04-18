def calc(A,n,dp):
    if n==2:
        return A[0]+A[1]
    s=1000000000
    for i in range(0,n-1):
        B=[]
        B=A[0:i]
        B.append(A[i]+A[i+1])
        B=B+A[i+2:]
        if B in dp:
            s=min(s,A[i]+A[i+1]+dp[B])
        else:
            d=calc(B,n-1,dp)
            s=min(s,A[i]+A[i+1]+d)
            dp[B]=d
            
    return s
n=int(input())
A=list(int(i) for i in input().split())
dp={}
calc(A,n,dp)
#for i in range(n):
