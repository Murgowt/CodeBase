def binomial(n,k):
	binomial=[[0 for x in range(n+1)] for x in range(n+1)] 
	print(binomial)
	for i in range(n+1):
		for j in range(min(i,k)+1):
			if(j==0 or i==j):
				binomial[i][j]=1
			else:
				binomial[i][j]=binomial[i-1][j-1]+binomial[i-1][j]
	print(binomial[n][k],binomial)

n=int(input())
k=int(input())
binomial(4,2)