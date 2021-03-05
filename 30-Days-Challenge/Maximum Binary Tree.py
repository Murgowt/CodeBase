# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def Build(nums):
    if(len(nums) ==0 ):
        return(None)
    
    pos=nums.index(max(nums))
    
    root=TreeNode(max(nums))
    root.left=Build(nums[:pos])
    root.right=Build(nums[pos+1:])
    
    return(root)
    
    
    
    
    
    
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root=Build(nums)
        return(root)
