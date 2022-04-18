#FOR HEAP THE PARENT VALUE IS GREATER THAN THE CHILD
#FOR MAXHEAP YOU CAN ONLY INCREASE THE VALUE OF A node
#IF YOU WANT TO DECREASE THE VALUE YOU HAVE TO BUILD MIN HEAP
#IT IS BASICALLY USED TO FIND THE MAX IN O1
#BINARY HEAP/PRIORITY QUEUE
INT_MAX=10**11+7
MOD=10**9+7
def INPUT():return list(int(i) for i in input().split())
def LIST_1D_ARRAY(n):return [0 for _ in range(n)]
def LIST_2D_ARRAY(m,n):return [[0 for _ in range(n)]for _ in range(m)]
#=======================================================================
n=5
B=[20,18,15,13,12]
A=[0]
A.extend(B)
def maxheapify(A,i,n):
    left=2*i
    right=2*i+1
    if left<=n and A[left]>A[i]:
        largest=left
    else:largest=i
    if right<=n and A[right]>A[largest]:
        largest=right
    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        maxheapify(A,largest,n)

for i in range(n//2,0,-1):
    maxheapify(A,i,n)

def update(A,i,val):
    A[i]=val
    while(i>1 and A[i//2]<A[i]):
        A[i//2],A[i]=A[i],A[i//2]
        i//=2
def extractmax(A,n):
    if n==0:
        return
    max=A[1]
    A[1]=A[n]
    n-=1
    maxheapify(A,1,n-1)
    return max
print(A)
q=int(input())
for _ in range(q):
    s=list(int(i) for i in input().split())
    if s[0]==2:
        print(A[1])
    else:
        val=s[1]
        A.append(-1)
        n+=1
        update(A,n,val)
        print(A)
print(A)
