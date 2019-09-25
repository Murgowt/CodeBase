import time
import os

os.chdir(r'C:/Users/Pollam/Desktop/CodeBase/Sorting')
string=list(open('test.txt'))
l=list(map(int,string[0].split()))
start=time.time()
def swap(l,i):
    temp=l[i]
    l[i]=l[i+1]
    l[i+1]=temp
    return(l)
n=len(l)
for j in range(n-1,-1,-1):
    for i in range(j):
        if(l[i]>l[i+1]):
            l=swap(l,i)

print("Time: ",time.time()-start)
        
