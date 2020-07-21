#O(n^2)
def Catalan(n):
    catalan=[0]*n
    catalan[0],catalan[1]=1,1
    for i in range(2,n):
        for j in range(i):
            catalan[i]+=catalan[j]*catalan[i-1-j]
    print(catalan[n-1])
    print(catalan)

n=int(input())
Catalan(n)

