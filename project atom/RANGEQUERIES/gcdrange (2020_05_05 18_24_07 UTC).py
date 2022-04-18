INT_MAX=10**19+7
MOD=10**12+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
#=======================================================================
import math as M
n=int(input())
A=INPUT()
k=int(M.log2(n))+1
st=[[0 for i in range(n)]for j in range(k)]
st[0]=A
for i in range(1,k):
    for j in range(n-2**(i-1)):
        st[i][j]=M.gcd(st[i-1][j],st[i-1][j+2**(i-1)])

for ele in st:print(ele)
for _ in range(int(input())):
    l,r=INPUT()
    ans=0
    for i in range(k-1,-1,-1):
        if l+2**i-1<=r:
            ans=M.gcd(ans,st[i][l])
            l+=2**i
    print(ans)
