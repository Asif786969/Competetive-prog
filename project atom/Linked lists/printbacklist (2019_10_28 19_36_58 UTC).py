class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def craetell(arr):
    if(len(arr)==0):
        return None
    head=Node(arr[0])
    last=head
    for data in arr[1:]:
        last.next=Node(data)
        last=last.next
    return head
def printll(head):
    if(head==None):
        return None
    head.next=printll(head.next)
    print(head.data,end=" ")

#A=list(int(i) for int i input().split(" "))
A=[1,2,3,4,5,-1]
L=craetell(A[:-1])
printll(L)
