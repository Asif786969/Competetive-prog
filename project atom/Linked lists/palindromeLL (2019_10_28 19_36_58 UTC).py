class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def check_palindrome(head) :
    #############################
    temp=head
    last=head
    l=createoppll(last)
    d=0
    while temp.next is not None:
        temp=temp.next
    last=temp
    while head.next is not None:
        if(head.data!=last.data):
            d=1
            break
        head=head.next
        last.next=last

    if(d==0):
        print("Palindrome")
    else:
        print("Not Palindrome")


    #############################
def createoppll(head,A):
    if head is None:
        return None
    head=head.dat




def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")
