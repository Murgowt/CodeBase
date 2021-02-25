class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero,one,two=0,0,0
        for i in nums:
            if(i is 1):
                one+=1
            elif(i is 2):
                two+=1
            else:
                zero+=1
        j=0
        for i in range(zero):
            nums[j]=0
            j+=1
        for i in range(one):
            nums[j]=1
            j+=1
        for i in range(two):
            nums[j]=2
            j+=1
        return(nums)
