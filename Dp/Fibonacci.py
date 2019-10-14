#Dynammic Programming-Memoization Algorithm
#Time=(No of Subproblems)*(Time taken by each Sub-Problem) #(Dont count Recursions)



#FIBONNACI SERIES

#NAIVE RECURION--Exponential Time
def fib(n):
    if(n==1 or n==0):
        return 1
    else:
        return fib(n-1) + fib(n-2)
#T(n)=T(n-2)+T(n-2)+c
n=int(input('Enter the Value of n: '))
print(fib(n-1))

#Going to Improvise based on Memoized DP algorithm Method:
#We create a Dictionary and enter the N-th value
# While Execution if the value is in the Dictionary well and good
# else compute and insert into the dictionary

#Memoized DP algorithm--Constant Time
def dfib(n):
    if(n in m.keys()):
        return m[n]
    else:
        if(n==1 or n==0):
            m[n]=1
            return 1
        else:
            f= fib(n-1) + fib(n-2)
            m[n]=f
            return f

m={}
n=int(input('Enter the Value of n: '))
print(dfib(n-1))
