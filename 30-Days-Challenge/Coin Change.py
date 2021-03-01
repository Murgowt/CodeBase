def PRINT(dp):
    for i in dp:
        for j in i:
            print(j,end=" ")
        print("")

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf') for i in  range(amount+1)]
        dp[0]=0
        for i in range(amount+1):
            for j in coins:
                if(j<=i):
                    sub_res=dp[i-j]
                    if(sub_res!=float('inf') and sub_res+1<dp[i]):
                        dp[i]=sub_res+1
        print(dp)
        if(dp[amount]==float('inf')):
            return(-1)
        return(dp[amount])
