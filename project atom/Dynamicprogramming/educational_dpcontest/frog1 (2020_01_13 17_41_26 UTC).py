n=int(input())
A=list(int(i) for i in input().split())
# n=6
# A=[30,10,60,10,60,50]
dpmincost=[0 for i in range(n)]
dpmincost[0]=0
dpmincost[1]=abs(A[1]-A[0])
for i in range(2,n):
    dpmincost[i]=min(dpmincost[i-1]+abs(A[i]-A[i-1]),dpmincost[i-2]+abs(A[i]-A[i-2]))
print(dpmincost[-1])
