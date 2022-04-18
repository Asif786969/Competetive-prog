v,roads=list(int(i) for i in input().split(" "))
A=[[0 for i in range(v)] for j in range(v)]
def dfs(A,initial,k,v):
    for i in range(v+1):
        
for i in range(roads):
    a,b=list(int(i) for i in input().split(" "))
    A[a][b]=1
    A[b][a]=1
print("Enter the vertex to be searched for path exist")
initial=int(input())
k=int(input())
dfs(A,initial,k,v)
