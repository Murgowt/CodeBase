import os
import time

os.chdir(r'C:\Users\Pollam\Desktop\CodeBase\Searching')
string=list(open('test.txt'))
l=list(map(int,string[0].split()))
n=len(l)
start=time.time()
def Binary_Search(s,low,high):
    
    mid=(low+high)//2
   
    if(mid==0 or mid==n or low==high or mid==low or mid==high):
        print("Element Not in the Given List")
        return
    else:
        if(l[mid]>s):
            print('low',l[mid],low,high)
            Binary_Search(s,low,mid)
        elif(l[mid]<s):
            print(l[mid],'high',low,high)
            Binary_Search(s,mid,high)
        else:
            print('Found the Element',s,'at the Position: ',mid+1)

s=int(input("Enter the Number to Be searched"))
Binary_Search(s,0,n-1)

end=time.time()
print(end-start)
