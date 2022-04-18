#POWER TO ANSWER THE RANGE QUERIES IN O1 OR O(LOGN)
#DRAWBACK IS THAT IT CAN BE USED ONLY FOR THE IMMUTABLE ARRAYS/
#WE CAN WRITE THE RANGE AS THE SUMMATION OF DECREASING POWERS OF 2
#ST[I][J] WILL STORE THE RANGE OF I,I+2^J-1
#RMQ

inf=10**9+7
import math as M
n=int(input())
A=list(int(i) for i in input().split())
#q=int(input("Enter the no of queri"))
st=[[inf for i in range(n)] for j in range(int(M.log2(n))+1)]
for i in range(n):
    st[0][i]=A[i]
for i in range(1,int(M.log2(n))+1):
    j=0
    for j in range(n-2**(i-1)):
            st[i][j]=min(st[i-1][j],st[i-1][j+2**(i-1)])
print(*st)

q=int(input())
for _ in range(q):
    l,r=list(int(i) for i in input().split())
    k=int(M.log2(r-l+1))
    print(min(st[k][l],st[k][r-2**k+1]))
