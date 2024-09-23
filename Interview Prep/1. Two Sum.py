class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht={}
        for i in range(len(nums)):
            counter = target - nums[i]
            if(ht.get(counter) is None):
                ht[nums[i]]=i
            else:
                return [i,ht[counter]]