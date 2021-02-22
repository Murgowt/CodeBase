class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(m)] for j in range(n)]
        for i in range(m):
            dp[0][i]=1
        for i in range(n):
            dp[i][0]=1
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        for i in dp:
            for j in i:
                print(j,end=" ")
            print("")
        
        return(dp[n-1][m-1])
