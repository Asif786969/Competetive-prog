class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
# def printtree(rootnode):
#     if(rootnode==N
def printtree(root):
    if(root==None):
        return
    print(root.data,end=":")
    if(root.left!=None):
        print("L",root.left.data, end=",")
    if(root.left!=None):
        print("R",root.right.data, end="")
    print()
    printtree(root.left)
    printtree(root.right)
def takeinput():
    rootdata=input()
    if(rootdata==-1):
        return None
    root=Node(rootdata)
    root.left=takeinput()
    root.right=takeinput()
    return root
root=takeinput()
printtree(root)
