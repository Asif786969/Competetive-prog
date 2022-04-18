import sys
#n,k=list(int(i) for i in input().split())
#A=list(int(i) for i in input().split())
n,k=10,4
A=[40,10,20,70,80,10,20,70,80,60]
dpmincost=[0 for i in range(n)]
dpmincost[0]=0
for i in range(1,n):
    x=sys.maxsize
    for j in range(1,k+1):
        if i-j>=0:
            x=min(dpmincost[i-j]+abs(A[i]-A[i-j]),x)
    dpmincost[i]=x
print(dpmincost)
