import time
import os

os.chdir(r'C:/Users/Pollam/Desktop/CodeBase/Sorting')
string=list(open('test.txt'))
l=list(map(int,string[0].split()))
start=time.time()
def swap(l,i,j):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    return(l)
n=len(l)
for i in range(n):
    min=l[i]
    index=i
    for j in range(i,n):
        if(l[j]<min):
            index=j
            min=l[j]
    if(index!=i):
        swap(l,i,index)


print(l)
print("Time: ",time.time()-start)
