print("Enter no of vetexes:",end=" ")
n=int(input())
print("Enter no of edges:",end=" ")
e=int(input())
A=[[],[],[],[],[],[]]
print("Enter the starting vetexxes and ending vertexes:")
for i in range(e):
    sv,ev=list(int(i) for i in input().split())
    A[sv].append(ev)
    A[ev].append(sv)
print(A)
#A=[] and for k in range(k+1):A.append([])
