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


val=[20,5,10,40,15,25]
wgt=[1,2,3,8,7,4]
n=6
count=0
W=10
dp=[[-1 for i in range(W+1)] for i in range(n+1)]
print("Maximum Profit: ",KnackSack(val,wgt,n,W))