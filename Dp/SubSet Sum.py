def PrintDP(dp):
	for i in dp:
		for j in i:
			print(j,end="\t")
		print("")

def Subset(n,S,arr):
	dp=[[-1 for i in range(S+1)] for j in range(n+1)]

	for i in range(S+1):
		dp[0][i]=False

	for j in range(n+1):
		dp[j][0]=True

	for i in range(1,n+1):
		for j in range(1,S+1):
			if(arr[i-1]>j):
				dp[i][j]=dp[i-1][j]
			else:
				dp[i][j]= dp[i-1][j] or dp[i-1][j-arr[i-1]]
	PrintDP(dp)
	return(dp[n][S])


arr=[7,3,2,5,8]
S=14
print(Subset(5,14,arr))
