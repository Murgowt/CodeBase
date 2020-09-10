def PrintDP(dp):
	for i in dp:
		for j in i:
			print(j,end="\t")
		print("")
		
#Recursive Approach
def UnBoundedKS(W,val,wt,n):
	if(W==0 or n==0):
		return(0)

	if(W<wt[n-1]):
		return(UnBoundedKS(W,val,wt,n-1))

	else:
			#Item Ignored			  #Item Taken
		return(max(UnBoundedKS(W,val,wt,n-1),UnBoundedKS(W-wt[n-1],val,wt,n)+val[n-1]))

#Iterative DP Approach
 def UnBoundedKS(W,val,wt,n):
	dp=[[-1 for i in range(W+1)] for j in range(n+1)]

	for i in range(W+1):
		dp[0][i]=0
	for i in range(n+1):
		dp[i][0]=0
	for i in range(1,n+1):
		for j in range(1,W+1):
			if(wt[i-1]>j):
				dp[i][j]=dp[i-1][j]
			else:
				dp[i][j]=max(dp[i][j-wt[i-1]]+val[i-1],dp[i-1][j])

	PrintDP(dp)
	return(dp[i][j])


W=100
val=[1,30]
wt=[1,50]
print(UnBoundedKS(W,val,wt,2))
