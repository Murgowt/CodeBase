def MinJumps(arr,n):
	jumps=[float('inf') for i in range(n)]
	jumps[0]=0
	for i in range(n):
		for j in range(i):
			if(j+arr[j]>=i):
				if(jumps[j]+1<jumps[i]):
					jumps[i]=jumps[j]+1

	print(jumps)
	return(jumps[n-1])

arr=[1,3,5,8,9,2,6,7,6,8,9]
print(MinJumps(arr,11))