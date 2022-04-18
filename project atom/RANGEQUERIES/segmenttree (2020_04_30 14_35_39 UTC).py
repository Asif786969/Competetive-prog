from random import randint
import segmenttree
def segmenttree(A,T,s,e,node):
    if s==e:
        T[node]=A[s]
        return
    mid=(s+e)//2
    segmenttree(A,T,s,mid,2*node)
    segmenttree(A,T,mid+1,e,2*node+1)
    T[node]=T[2*node] + T[2*node + 1]

n=int(input())
#A=list(int(i) for i in input().split())
A=[randint(-10**9,10**9) for i in range(n)]
T=[0 for i in range(4*n)]
segmenttree(A,T,0,n-1,1)
#print(T)
