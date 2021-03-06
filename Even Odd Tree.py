# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def ODD(l):
    if(len(l)==1):
        return(l[0]%2==0)
    for i in range(1,len(l)):
        if(not(l[i]<l[i-1] and l[i]%2==0) ):
            return(False)
    return(True)

def EVEN(l):
    if(len(l)==1):
        return(l[0]%2!=0)
    for i in range(1,len(l)):
        if(not (l[i]>l[i-1] and l[i]%2!=0) ):
            return(False)
    return(True)

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
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
        for i in queue:
            temp=[]
            for j in i:
                temp.append(j.val)
            lot.append(temp)
        print(lot)
        for i in range(len(lot)):
            if(i%2==0):
                print("EVEN")
                flag=EVEN(lot[i])
            else:
                print("ODD")
                flag=ODD(lot[i])
            print(flag)
            if(not flag):
                return(False)
        return(True)
                
