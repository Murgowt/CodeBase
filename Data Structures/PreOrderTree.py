class Node:
	def __init__(self,val):
		self.val=val
		self.left=None
		self.right=None


def Convert(preorder):
	if(len(preorder)==0):
		return None
	node=Node(preorder[0])
	i=1
	while(i<len(preorder)):
		if(preorder[i]>preorder[0]):
			break
		i+=1
	node.left=Convert(preorder[1:i])
	node.right=Convert(preorder[i:])

	return(node)


def Inorder(root):
	if(root==None):
		return []
	left=Inorder(root.left)
	right=Inorder(root.right)
	return(left+[root.val]+right)


preorder=[4,5,2,6,3,1]
root=Convert(preorder)
print("Inorder traversal of the Tree : ",Inorder(root))