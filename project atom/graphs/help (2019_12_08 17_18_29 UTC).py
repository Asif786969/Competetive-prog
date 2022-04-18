def connected(M,n,visited,clib,crd):
    cost=0
    x=0
    for i in range(1,n+1):
        if(visited[i] is False):
            dfs(n,M,visited,i)
            x+=1
    print(x)
    cost=x*clib+(n-x)*crd
    print(cost)

def dfs(n,M,visited,sv):
    visited[sv]=True
    for i in range(1,n+1):
        if(i!=sv):
            if(visited[i] is False):
                if(M[sv][i]==1):
                    dfs(n,M,visited,i)



n,m,clib,crd=[100,3,4,3]
M=[[0 for l in range(n+1)]for t in range(n+1)]
#print(M)
C=[[88,34],[23,90],[23,89]]
for j in range(m):
    #s,e=list(int(i) for i in input().split())
    V=C[j]
    s=V[0]
    e=V[1]
    M[s][e]=1
    M[e][s]=1
#print(M)
if(crd>clib):
    cost=clib*n
    print(cost)
else:
    #remove excess roads
    visited=[False for i in range(n+1)]
    connected(M,n,visited,clib,crd)
