#Global N value For any Sqaure Dimensioned Board
n=8


def Valid(board,curr_x,curr_y):
	if(curr_x<n and curr_x>=0 and curr_y<n and curr_y>=0 and board[curr_x][curr_y]==-1):
		return True
	else:
		return False


def PrintBoard(board):
	for i in range(n):
		for j in range(n):
			print( board[i][j],end=" ")
		print("")

def Algorithm(board,curr_x,curr_y,xmove,ymove,pos):
	if(pos==n**2):
		return True
	else:
		for i in range(8):
			new_x=curr_x+xmove[i]
			new_y=curr_y+ymove[i]
			if(Valid(board,new_x,new_y)):
				board[new_x][new_y]=pos
				
				if(Algorithm(board,new_x,new_y,xmove,ymove,pos+1)):
					
					return True

				#BackTracking Back to previous position
				board[new_x][new_y]=-1
		return False



def Initializer():
	#Initializing Values
	board=[[-1 for i in range(n)]for j in range(n)]
	xmove=[1,2,2,1,-1,-2,-2,-1]
	ymove=[2,1,-1,-2,-2,-1,1,2]
	pos=0

	#Setting up the Starting Positions
	board[0][0]=0
	pos=1

	if(Algorithm(board,0,0,xmove,ymove,pos)):#board,curr_x,curr_y,xmove,ymove,pos
		PrintBoard(board)
	else:
		print("Solution Not Possible")





Initializer()