import time as T
def base(ele,k,B):
    r=ele%k
    if r not in B:
        B.append(r)
def calc(A,k,ele,B):
    for i in range(1,11):
        base(ele*i,k,B)
n,k=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
start=T.time()
A.sort()
B=[]
for ele in A:
    calc(A,k,ele,B)
#x=set(B)
B.sort()

print(len(B))
print(*B)
print(T.time()-start)