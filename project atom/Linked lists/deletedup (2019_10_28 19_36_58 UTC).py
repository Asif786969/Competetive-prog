class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    #  Given a sorted linked list (elements are sorted in ascending order).
    #  Eliminate duplicates from the given LL, such that output LL contains only
    #  unique elements.
    #############################
    temp=head
    t1=head
    t2=head.next
    while(t2.next is not None):
        if(t1.data==t2.data):
            t2=t2.next
        else:
            t1.next=t2
            t1=t2
            t2=t2.next
        if(t1.data==t2.data):
            t1.next=None
        else:
            t1.next=t2

    return temp

    #############################


def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = eliminate_duplicate(l)
printll(l)
