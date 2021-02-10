class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht={}
        for i in nums:
            ht[i]=target-i
        for i in ht.keys():
            if(ht[i] in ht.keys()):
                fi=nums.index(i)
                si=nums.index(ht[i])
                if(fi==si):
                    for j in range(len(nums)):
                        if(nums[j]==i and j!=fi):
                            si=j
                if(fi==si):
                    continue
                else:
                    return(fi,si)