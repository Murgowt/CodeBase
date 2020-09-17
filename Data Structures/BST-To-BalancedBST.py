class Node():
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

def AddNode(root,value):
    if(root.data>value):
        if(root.left==None):
            root.left=Node(value)
            return
        AddNode(root.left,value)
    else:
        if(root.right==None):
            root.right=Node(value)
            return
        AddNode(root.right,value)

def Inorder(root):
    global inorderseq
    if(root==None):
        return
    Inorder(root.left)
    inorderseq.append(root.data)
    Inorder(root.right)

def PreOrder(root):
    if(root==None):
        return
    print(root.data,end=" ")
    PreOrder(root.left)
    PreOrder(root.right)

def BalancedBST(seq):

    if not seq:
        return None
    mid=len(seq)//2
    root=Node(seq[mid])
    root.left=BalancedBST(seq[:mid])
    root.right=BalancedBST(seq[mid+1:])
    return(root)

arr=[1,2,3,4,5,6,7]
inorderseq=[]
root=None
for i in arr:
    if(root==None):
        root=Node(i)
    else:
        AddNode(root,i)
Inorder(root)
NewRoot=BalancedBST(inorderseq)
PreOrder(NewRoot)
