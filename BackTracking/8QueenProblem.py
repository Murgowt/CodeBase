def PrintBoard(board):
	for i in board:
		for j in i:
			print(j ,end=" ")
		print('')

def Valid(board,row,col):
	for i in range(col):
		if(board[row][i]==1):
			return False
	tempx=row
	tempy=col
	while(tempx<8 and tempy <8 and tempx>=0 and tempy>=0):
		if(board[tempx][tempy]==1):
			return False
		tempx=tempx+1
		tempy=tempy-1

	tempx=row
	tempy=col
	while(tempx<8 and tempy <8 and tempx>=0 and tempy>=0):
		if(board[tempx][tempy]==1):
			return False
		tempx=tempx-1
		tempy=tempy-1

	return True

def Algorithm(board,col):
	if(col==8):
		return(True)
	for i in range(8):
		if(Valid(board,i,col)):
			board[i][col]=1
			if(Algorithm(board,col+1)):
				return True

			#Back-Track
			board[i][col]=0
	return False

def Initializer():
	board=[[0 for i in range(8)] for j in range(8)]
	if(Algorithm(board,0)):
		PrintBoard(board)
	else:
		print("Solution Not Possible")



Initializer()