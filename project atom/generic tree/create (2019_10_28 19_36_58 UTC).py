class Node:
    def __init__(self,data):
        self.data=data
        self.children=list()
def takeinput():
    print("Enter root data:")
    rootdata=int(input())
    if rootdata==-1:
        return
    root=Node(rootdata)
    print("Enter the no of children for ",rootdata)
    n=int(input())
    for i in range(n):
        child=takeinput()
        root.children.append(child)
    return root
def printtreedetail(root):
    if root is None:
        return
    print(root.data,":",end="")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printtreedetail(child)
def numnodes(root):
    if root is None:
        return 0
    count=1
    for child in root.children:
        count+=numnodes(child)
    return count
def maxi(root):
    if root is None:
        return None
    maximum=root.data
    for child in root.children:
        maximum=max(maximum,maxi(child))
    return maximum
root=takeinput()
printtreedetail(root)
print(maxi(root))
