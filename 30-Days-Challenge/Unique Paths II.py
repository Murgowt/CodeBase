class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid[0])
        n=len(obstacleGrid)
        dp=[[-1 for i in range(m)] for j in range(n)]
        inc=1
        for i in range(m):
            if(obstacleGrid[0][i]==1):
                dp[0][i]=0
                inc=0
            else:
                dp[0][i]=inc
        inc=1
        for i in range(n):
            if(obstacleGrid[i][0]==1):
                dp[i][0]=0
                inc=0
            else:
                dp[i][0]=inc
        
        for i in range(1,n):
            for j in range(1,m):
                if(obstacleGrid[i][j]==1):
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
        
        return(dp[n-1][m-1])
