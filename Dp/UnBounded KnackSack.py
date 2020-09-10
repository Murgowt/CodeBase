def UnBoundedKS(W,val,wt,n):
	if(W==0 or n==0):
		return(0)

	if(W<wt[n-1]):
		return(UnBoundedKS(W,val,wt,n-1))

	else:
			#Item Ignored			  #Item Taken
		return(max(UnBoundedKS(W,val,wt,n-1),UnBoundedKS(W-wt[n-1],val,wt,n)+val[n-1]))




W=100
val=[1,30]
wt=[1,50]
print(UnBoundedKS(W,val,wt,2))
