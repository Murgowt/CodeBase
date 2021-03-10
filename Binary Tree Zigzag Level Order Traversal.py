# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if(root == None):
            return
        queue=[[root]]
        front=0
        while(front<len(queue)):
            temp=[]
            for j in queue[front]:
                if(j.left!=None):
                    temp.append(j.left)
                if(j.right!=None):
                    temp.append(j.right)
            if(len(temp)!=0):
                queue.append(temp)
            front+=1
        lot=[]
        count=1
        for i in queue:
            temp=[]
            for j in i:
                temp.append(j.val)
            if(count%2==0):
                lot.append(temp[::-1])
            else:
                lot.append(temp)
            count+=1
        return(lot)
