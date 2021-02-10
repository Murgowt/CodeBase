class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d={}
        for i in range(numRows):
            d[i]=''
        ct=0
        diff=1
        counter=0
        while(ct<len(s)):
            if(counter%numRows==numRows-1):
                diff=-1
                print(s[ct])
            if(counter%numRows==0):
                diff=1
            d[counter%numRows]+=s[ct]
            ct+=1
            counter+=diff
        op=''
        for i in d.keys():
            op+=d[i]
        print(op)
        return(op)
