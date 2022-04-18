import time as T
def base(ele,k,B):
    r=ele%k
    if r not in B:
        B.append(r)
def calc(A,k,ele,B,n):
    for i in range(0,n+1):
        base(ele*i,k,B)
n,k=list(int(i) for i in input().split())
A=list(int(i) for i in input().split())
start=T.time()
A.sort()
B=[]
for ele in A:
    calc(A,k,ele,B,n)
#x=set(B)
B.sort()
print(len(B))
print(*B)
print(T.time()-start)
