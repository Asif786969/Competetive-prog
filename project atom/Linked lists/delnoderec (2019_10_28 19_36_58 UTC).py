class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def linked(arr):
    if(len(arr)==0):
        return None
    head=Node(arr[0])
    last=head
    for data in arr[1:]:
        last.next=Node(data)
        last=last.next
    return head
def printll(head):
    while head:
        print(head.data,end=" ")
        head=head.next
    print()
def delrec(head,i):
    if(i<0):
        return head
    elif(head is None):
        return None
    if(i==0):
        return head.next
    smallhead=delrec(head.next,i-1)
    head.next=smallhead
    return smallhead

A=list(int(i) for i in input().split(" "))
i=int(input())
l=linked(A[:-1])
l=delrec(l,i)
printll(l)
