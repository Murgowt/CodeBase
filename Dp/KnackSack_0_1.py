# Number of Recurcive Function Calls Without Memoization=57
# Number of Recurcive Function Calls With Memoization =24

def KnackSack(val,wgt,n,W):
	global dp,count
	

	#Base Condition
	if(n==0 or W==0):
		return(0)
	#Choice Diagram
	if(not dp[n][W]==-1):
		return(dp[n][W])
	count+=1
	print(count)
	if(wgt[n-1]>W):
		return(KnackSack(val,wgt,n-1,W))
	else:
				     #Item Excluded			  #Item Not Included
		dp[n][W]=max(KnackSack(val,wgt,n-1,W),KnackSack(val,wgt,n-1,W-wgt[n-1])+val[n-1])
		return(dp[n][W])


def PrintDP(dp):
	for i in dp:
		for j in i:
			print(j,end='\t')
		print("")
		
# Top-Down  Approach
def TopDown(wgt,val,W,n):
	dp=[[-1 for i in range(W+1)]for j in range(n+1)]
	for i in range(W+1):
		dp[0][i]=0
	for i in range(n+1):
		dp[i][0]=0
	
	for i in range(1,n+1):
		for j in range(1,W+1):
			if(wgt[i-1]>j):
				dp[i][j]=dp[i-1][j]
			else:
				dp[i][j]=max(dp[i-1][j],dp[i-1][j-wgt[i-1]]+val[i-1])
	PrintDP(dp)

val=[20,5,10,40,15,25]
wgt=[1,2,3,8,7,4]
n=6
count=0           #To count the number of times the recurcive Function is being caled
W=10
dp=[[-1 for i in range(W+1)] for i in range(n+1)]
print("Maximum Profit: ",KnackSack(val,wgt,n,W)) 
