class Node:
    def __init__(self,Data=None):
        self.data=Data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.Root=Node()
    def CreateNewNode(self,root):
        pass
    def Tright(self,root):
        pass
    def create(self,root,Dalue):
        pass
    def fpass(self,root):
        pass
    def create(self,root,Data):
        if(self.Root.data==None):
            self.Root.data=Data
        else:
            node=Node(Data)
            if(Data>root.data):
                if(root.right==None):
                    root.right=node
                else:
                    self.create(root.right,Data)
            elif(Data<root.data):
                if(root.left==None):
                    root.left=node
                else:
                    self.create(root.left,Data)
            else:
                print("Duplicate Values")
                
    def CreateNewNode(self,root):
        Data=int(input("Enter Value: "))
        self.create(self.Root,Data)
    
    def inorder(self,root):
        if(root==None):
            return
        else:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def postorder(self,root):
        if(root==None):
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def preorder(self,root):
        if(root==None):
            return
        else:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
tree=Tree()
if(tree.Root.data==None):
    print("true")
switcher={1:tree.CreateNewNode,2:tree.inorder,3:tree.preorder,4:tree.postorder,5:tree.fpass}
ch=0
while(ch!=5):
    print("\n")
    ch=int(input("Enter your Choice:\n1.Insert New Value\n2.INorder Traversal\n3.Pre-Order Traversal\n4.Post-Order Traversal\n5.Exit\nEnter Your Choice:  "))
    switcher.get(ch,"Invalid Choice")(tree.Root)
