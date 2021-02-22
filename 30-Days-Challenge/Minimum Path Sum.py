def PRINT(dp):
    for i in dp:
        for j in i:
            print(j,end=" ")
        print("")
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        dp=[[-1 for i in range(m)] for j in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[0][i]=grid[0][i]+dp[0][i-1]
        for i in range(1,n):
            dp[i][0]=grid[i][0]+dp[i-1][0]
        
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        PRINT(dp)
        return(dp[n-1][m-1])
