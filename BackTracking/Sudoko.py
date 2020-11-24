def PrintSudoko(sudoko):
	for i in sudoko:
		for j in i:
			print(j,end=" ")
		print("")

def Valid(sudoko,row,col,num):
	if(num in sudoko[row]):
		return False
	for i in sudoko:
		if(num==i[col]):
			return False
	box=[[0,1,2],[3,4,5],[6,7,8]]
	row_index=row//3
	col_index=col//3
	for i in box[row_index]:
		for j in box[col_index]:
			if(num==sudoko[row][col]):
				return False
	return True
def Algorithm(sudoko,numbers,row,col,pos):
	print(row,col)
	if(pos>81):
		return True
	else:
		if(sudoko[row][col]==0):
			for num in numbers:
				if(Valid(sudoko,row,col,num)):
					sudoko[row][col]==num

					next_x=row+1
					if(next_x==9):
						next_x=0
						col+=1
						if(Algorithm(sudoko,numbers,next_x,col,pos+1)):
							return True
			sudoko[row][col]=0
			return False
		else:
			next_x=row+1
			if(next_x==9):
				next_x=0
				col+=1
				if(Algorithm(sudoko,numbers,next_x,col,pos+1)):
					return True
			return False


def Initializer():
	sudoko=[[3,0,6,5,0,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[0,0,3,0,1,0,0,8,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[1,3,0,0,0,0,2,5,0],[0,0,0,0,0,0,0,7,4],[0,0,5,2,0,6,3,0,0]]
	numbers=[1,2,3,4,5,6,7,8,9]
	pos=0
	row,col=0,0
	if(Algorithm(sudoko,numbers,row,col,pos+1)):
		PrintSudoko(sudoko)
	else:
		print("Solution Not Possible")


Initializer()