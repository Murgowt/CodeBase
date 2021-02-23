def search(row,matrix,target,n,m):
    low,high=0,m-1
    print(row)
    while(low<=high):
        mid=(low+high)//2
        if(matrix[row][mid]==target):
            return(True)
        if(matrix[row][mid]>target):
            high=mid-1
        else:
            low=mid+1
    return(False)
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(len(matrix)==0 or len(matrix[0])==0):
            return(False)
        row=0
        m=len(matrix[0])
        n=len(matrix)
        while(row<n):
            if(matrix[row][m-1]>=target):
                return(search(row,matrix,target,n,m))
            row+=1
        return(False)
