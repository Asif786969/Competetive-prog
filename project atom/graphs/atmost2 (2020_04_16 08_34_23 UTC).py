#FOR ATMOST 2 EDGES BETWEEEN U AND V
v=int(input("Enter the no of vertex:"))
e=int(input("Enter the no of edges:"))
A=[[] for i in range(v)]
for _ in range(e):
    sv,ev=list(int(i)for i in input().split())
    A[sv].append(ev)
for i in range(v):
    print(i,end="-> ")
    for j in range(len(A[i])):
        print(A[i][j],end=" ")
    print()

print()
result=[[] for i in range(v)]
for i in range(v):
    for j in range(len(A[i])):
        result[i].append(A[i][j])
        for k in range(len(A[A[i][j]])):
            if A[A[i][j]][k] not in result[i]:
                result[i].append(A[A[i][j]][k])
for i in range(v):
    print(i,end="-> ")
    for j in range(len(result[i])):
        print(result[i][j],end=" ")
    print()
