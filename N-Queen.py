N=int(input())
board=[[0]*N for i in range(N)]


def solve():
	global board
	if(solveRec(0)==False):
		return False
	else:
		for i in board:
			print(*i)
		return True
def solveRec(col):
	global N
	global board
	if col>=N:
		return True
	for i in range(N):
		if isSafe(i,col):
			board[i][col]=1
			if(solveRec(col+1)==True):
				return True
			board[i][col]=0
	return False
def isSafe(row,col):
	global N
	global board
	for i in range(0,col):
		if board[row][i]==1:
			return False
	for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
		if board[i][j]==1:
			return False
	for i,j in zip(range(row,N,1),range(col,-1,-1)):
		if board[i][j]==1:
			return False

	return True
print(solve())
