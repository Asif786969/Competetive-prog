v=int(input())
e=int(input())
A=[[0 for _ in range(v)]for _ in range(v)]
G=[[0 for _ in range(v)]for _ in range(v)]
for i in range(e):
    sv,ev=list(int(i) for i in input().split())
    A[sv][ev]=1
for i in range(v):
    for j in range(v):
        if A[i][j]==1:
            G[i][j]=1
            for k in range(v):
                if A[j][k]==1:
                    G[i][k]=1
for i in range(v):
    for j in range(v):
        print(A[i][j],end=" ")
    print()
print()
print()
for i in range(v):
    for j in range(v):
        print(G[i][j],end=" ")
    print()
