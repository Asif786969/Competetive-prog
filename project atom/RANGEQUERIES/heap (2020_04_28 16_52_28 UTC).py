#FOR HEAP THE PARENT VALUE IS GREATER THAN THE CHILD
N=int(input())
A=list(int(i) for i in input().split())
B=[0]
B.extend(A)
#building a max heapify
print(A)
def maxheapify(B,i):
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
        maxheapify(B,largest)
for i in range(N//2,0,-1):
    maxheapify(B,i)
print(B)
