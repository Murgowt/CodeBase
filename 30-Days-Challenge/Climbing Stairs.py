class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==1):
            return(1)
        stairs=[0]*n
        stairs[0],stairs[1]=1,2
        for i in range(2,n):
            stairs[i]=stairs[i-1]+stairs[i-2]
            
        return(stairs[n-1])
