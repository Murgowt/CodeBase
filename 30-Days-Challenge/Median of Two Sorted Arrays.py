class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fin=sorted(nums1+nums2)
        if(len(fin)%2==0):
            mid=len(fin)//2
            return((fin[mid-1]+fin[mid])/2)
        else:
            mid=len(fin)//2
            return(fin[mid])
