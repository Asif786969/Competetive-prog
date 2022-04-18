n=int(input())
A=list(int(i) for i in input().split())
import math as M
st=[[0 for i in range(n)]for j in range(int(M.log2(n))+1)]
st[0]=A
for i in range(1,int(M.log2(n))+1):
    for j in range(n-2**(i-1)):
        st[i][j]=st[i-1][j]*st[i-1][j+2**(i-1)]
print(st)
