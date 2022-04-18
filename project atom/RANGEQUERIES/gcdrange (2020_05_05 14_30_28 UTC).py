import math as M
n=int(input())
A=list(int(i) for i in input().split())
k=int(M.log2(n))+1
st=[[0 for i in range(k)]for t in range(n)]
for i in range(n):
    st[i][0]=A[i]

for j in range(1,k+1):
    for i in range(n-(1<<j)+1):
        st[i][j]=M.gcd(st[i][j-1],st[i-(1<<(j-1))][j-1])
for i in range(int(input())):
    l,r=list(int(i) for i in input().split())
    ans=0
    for j in range(k,-1,-1):
        if (l+(1<<j)-1)<=r:
            ans=M.gcd(ans,st[l][j])
            l+=1<<j
    print(ans)
