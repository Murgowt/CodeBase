# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
 #        self.right = None

def LCA(root,p,q):
    if(root.val==p.val or root.val==q.val):
        return(root)
    if(root.val>=p.val and root.val<=q.val):
        return(root)
    if(root.val >= p.val and root.val >= q.val):
        return(LCA(root.left,p,q))
    if(root.val<=p.val and root.val <=q.val):
        return(LCA(root.right,p,q))
        

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(p.val<q.val):
            return(LCA(root,p,q))
        else:
            return(LCA(root,q,p))
            
