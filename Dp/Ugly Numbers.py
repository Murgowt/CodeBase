def Ugly(n):
	ugly=[1]
	i2,i3,i5=0,0,0
	two,three,five=2,3,5
	curr=0
	while(len(ugly)<n):
		ugly.append(min(two,three,five))
		curr+=1
		if(ugly[curr]==two):
			i2+=1
			two=ugly[i2]*2
		if(ugly[curr]==three):
			i3+=1
			three=ugly[i3]*3
		if(ugly[curr]==five):
			i5+=1
			five=ugly[i5]*5

	return(ugly[curr])



n=int(input())
print(Ugly(n))