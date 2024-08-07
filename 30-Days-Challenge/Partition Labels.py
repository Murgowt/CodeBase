class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        end  = s.rfind(s[0])
        curr = end
        ans=[]
        for i in range(1,len(s)):
            if(i>curr):
                ans.append(end-start+1)
                start = i
                

            end = s.rfind(s[i])
            curr= max(curr,end)
        if(ans!=len(s)):
            ans.append(len(s)-start)
        return ans
