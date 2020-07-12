def Merge(lft,rgt):
	i,j=0,0
	arr=[]
	while(i<len(lft) and j<len(rgt)):
		if(lft[i]<rgt[j]):
			arr.append(lft[i])
			i+=1
		else:
			arr.append(rgt[j])
			j+=1
	while(i<len(lft)):
		arr.append(lft[i])
		i+=1
	while(j<len(rgt)):
		arr.append(rgt[j])
		j+=1
	return (arr)

def MergeSort(arr):
	l,r=0,len(arr)
	if(l<r and len(arr)>1):
		m=l+(r-l)//2
		lft=MergeSort(arr[l:m])
		rgt=MergeSort(arr[m:r])
		return (Merge(lft,rgt))
	else:
		return (arr)



l=list(map(int,input().split()))
print(MergeSort(l))