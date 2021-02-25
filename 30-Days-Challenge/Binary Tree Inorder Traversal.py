# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def Inorder(root):
    if(root is None):
        return([])
    
    return(Inorder(root.left)+[root.val]+Inorder(root.right))
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return(Inorder(root))
