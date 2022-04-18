def connected(M,n,visited,clib,crd):
    cost=0
    x=0
    for i in range(1,n+1):
        if(visited[i] is False):
            dfs(n,M,visited,i)
            x+=1
    cost+=x*clib+(n-x)*crd
    print(cost)

def dfs(n,M,visited,sv):
    visited[sv]=True
    for i in range(1,n+1):
        if(i!=sv):
            if(visited[i] is False):
                if(M[sv][i]==1):
                    dfs(n,M,visited,i)



q=int(input())
for i in range(q):
    n,m,clib,crd=list(int(i) for i in input().split())
    M=[[0]*(n+1)]*(n+1)
    for j in range(m):
        s,e=list(int(i) for i in input().split())
        M[s][e]=M[e][s]=1
    if(crd>clib):
        cost=clib*n
        print(cost)
    else:
        #remove excess roads
        visited=[False for i in range(n+1)]
        connected(M,n,visited,clib,crd)
