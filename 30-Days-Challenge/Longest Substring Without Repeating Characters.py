def SlidingWindow(s):
    if(len(s)==0):
        return(0)
    low,high=0,0
    begin,end=0,0
    freq={}
    while(high<len(s)):
        if(freq.get(s[high])==None):
            freq[s[high]]=1
        else:
            freq[s[high]]+=1
        while(freq[s[high]]>1):
            freq[s[low]]-=1
            low+=1
        if(high-low>end-begin):
            begin=low
            end=high
        high+=1
    return(end-begin+1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return(SlidingWindow(s))
