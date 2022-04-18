class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)
        return
    def searchhelper(self,root,data):
        if root is None:
            return False
        if root.data==data:
            return True
        if(root.data>data):
            return self.searchhelper(root.left,data)
        else :
            return self.searchhelper(root.right,data)


    def search(self, data):
        self.searchhelper(self.root,data)
    def inserthelper(self,root,data):
        if root is None:
            root=BinaryTreeNode(data)
            return root
        if root.data>data:
            root.left=self.inserthelper(root.left,data)
            return root
        else:
            root.right=self.inserthelper(root.right,data)
            return root
    def insert(self, data):
        self.root=self.inserthelper(self.root,data)
        self.numNodes+=1
    def min(self,root):
        if root is None:
            return 100000
        if root.left is None:
            return root.data
        return self.min(root.left)
    def deletehelper(self,root,data):
        if root is None:
            return False,None
        if root.data<data:
            deleted,newright=self.deletehelper(root.right,data)
            root.data=newright
            return deleted,root
        if root.data>data:
            deleted,newleft=self.deletehelper(root.left,data)
            root.left=newleft
            return deleted,root
        if root.left is None and root.right is None:
            return True,None
        if root.left is None:
            return True,root.right
        if root.right is None:
            return True,root.left
        replacement=self.min(root.right)
        root.data=replacement
        deleted,newright=self.deletehelper(root.right,replacement)
        root.right=newright
        return True,root

    def delete(self, data):
        deleted,newroot=self.deletehelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root=newroot
        return deleted

    def count(self):
        return self.numNodes
b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li))):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1

    
