def PrintTable(table):
	for i in table:
		for j in i:
			print(j,end=" ")
		print("")
	print("                         ")

#Bottom-Up Approach
def CoinChange(arr,n,m):
	table=[[-1 for i in range(n+1)]for j in range(m+1)]
	for i in range(m+1):
		table[i][0]=1
	for i in range(1,n+1):
		table[0][i]=0
	for i in range(1,m+1):
		for j in range(1,n+1):
			#Include the Coin
			if(j-arr[i-1]<0):
				x=0
			else:
				x=table[i][j-arr[i-1]]
			#Not Including the Coin
			y=table[i-1][j]
			table[i][j]=x+y
	print(table[m][n])
	PrintTable(table)


	
	
arr=[1,2,5]
n=5
m=len(arr)
CoinChange(arr,n,m)
TDtable=[[-1 for i in range(n+1)] for j in range(m+1)]

print(TDCoinChange(arr,n,m))
