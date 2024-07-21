def BellNumber(n):
	Bell=[[1]]
	for i in range(1,n+1):
		level=[]
		for j in range(i+1):
			if(j==0):
				level.append(Bell[i-1][i-1])
			else:
				temp=level[j-1]+Bell[i-1][j-1]
				level.append(temp)
		Bell.append(level)
	for i in Bell:
		for j in i:
			print(j,end=" ")
		print("")
	print(str(n)+"th Bell Numer is "+str(Bell[n][0]))

print("Hello World!")





n=int(input())
BellNumber(n)
