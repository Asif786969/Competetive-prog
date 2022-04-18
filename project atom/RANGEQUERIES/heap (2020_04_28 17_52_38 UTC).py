#FOR HEAP THE PARENT VALUE IS GREATER THAN THE CHILD
N=int(input())
A=list(int(i) for i in input().split())
B=[0]
B.extend(A)
#building a max heapify
print(A)
def maxheapify(B,i,N):
    left=2*i
    right=2*i+1
    if left<=N and B[left]>B[i]:
        largest=left
    else:
        largest=i
    if right<=N and B[largest]<B[right]:
        largest=right
    if largest!=i:
        B[i],B[largest]=B[largest],B[i]
        maxheapify(B,largest,N)

def increasevalue(B,val,i):
    if val<B[i]:
        return
    B[i]=val
    while(i>1 and B[i//2]<B[i]):
        B[i//2],B[i]=B[i],B[i//2]
        i//=2

def inserting(B,val,N):
    B.append(-1)
    N+=1
    increasevalue(B,val,N)

for i in range(N//2,0,-1):
    maxheapify(B,i,N)
print(B)
print()
val=int(input("Enter value to insert "))
inserting(B,val,N)
print(B)
