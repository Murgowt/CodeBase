class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if(x<0):
            sign=-1
            x=x*-1
        ans=0
        while(x>0):
            ans=ans*10+(x%10)
            x=x//10
        INT_MAX=(2**31)-1
        INT_MIN=-(2**31)
        print(INT_MAX,INT_MIN)
        if(ans<INT_MIN or ans> INT_MAX):
            return(0)
        return(ans*sign)
