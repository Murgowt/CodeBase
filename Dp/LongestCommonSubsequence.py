def PrintMatrix(LCS):
	for i in LCS:
		for j in i:
			print(j,end="\t")
		print("")


def Result(LCS,m,n,s1,s2):
	print("Length of Longest Common Subsequence is ",LCS[m][n])
	seq=''
	while(m!=0 and n!=0):
		top=LCS[m-1][n]
		left=LCS[m][n-1]
		if(LCS[m][n]==left):
			n-=1
		elif(LCS[m][n]==top):
			m-=1
		else:
			seq+=s1[n-1]
			n-=1
			m-=1
	seq=seq[::-1]
	print("The Longest Subsequence is ",seq)


def Algorithm(s1,s2,n,m,LCS):
	#Base Case 
	   #The 0th index is NIL 
	   #The LCS of NIL is 0
	#Dynamic Programming Algorithm
	   #SubCases
	      # if Last Characters Match
	      	#LCS=LCS(m-1,n-1)+1
	      #  else
	        # LCS=max(LCS(m-1,n),LCS(n+1,m))

	for i in range(m+1):
		for j in range(n+1):
			if(j==0 or i==0):
				LCS[i][j]=0
			elif(s1[j-1]==s2[i-1]):
				LCS[i][j]=LCS[i-1][j-1]+1
			else:
				LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
	
	Result(LCS,m,n,s1,s2)
	


def Initializer():
	s1=input()
	s2=input()
	n=len(s1)
	m=len(s2)
	LCS=[[-1 for i in range(n+1)]for j in range(m+1)]
#	PrintMatrix(LCS)
	Algorithm(s1,s2,n,m,LCS)

Initializer()