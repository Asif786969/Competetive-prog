import math as M
n=int(input())
A=list(int(i) for i in input().split())
k=16
st=[[0 for i in range(n)]for t in range(k)]
st[0]=A
print(st)
for j in range(1,k):
    for i in range(n-(1<<j)+1):
        print(i,j)
        st[j][i]=M.gcd(st[j][i-1],st[j+(1<<(i-1))][i-1])
print(st)
for i in range(int(input())):
    l,r=list(int(i) for i in input().split())
    ans=0
    for j in range(k,-1,-1):
        if (l+(1<<j)-1)<=r:
            ans=M.gcd(ans,st[l][j])
            l+=1<<j
    print(ans)
