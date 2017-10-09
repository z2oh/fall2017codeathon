M = input().split(' ')
M[0] = int(M[0])

R = int(input())
C = int(input())

board = [[None] * C] * R

for x in range(R):
	board[x] = list(map(int, input().split(' ')))

def removeZeroes(direction):
	if(direction == 'U'):
		for j in range(C):
			cols = [0] * R
			idx = 0
			for i in range(R):
				if(board[i][j] != 0):
					cols[idx] = board[i][j]
					idx += 1
			for i in range(R):
				board[i][j] = cols[i]
	elif(direction == 'D'):
		for j in range(C):
			cols = [0] * R
			idx = 0
			for i in range(R):
				if(board[R-i-1][j] != 0):
					cols[idx] = board[R-i-1][j]
					idx += 1
			for i in range(R):
				board[R-i-1][j] = cols[i]
	elif(direction == 'R'):
		for i in range(R):
			row = [0] * C
			idx = 0
			for j in range(C):
				if(board[i][C-j-1] != 0):
					row[idx] = board[i][C-j-1]
					idx += 1
			for j in range(C):
				board[i][C-j-1] = row[j]
	elif(direction == 'L'):
		for i in range(R):
			row = [0] * C
			idx = 0
			for j in range(C):
				if(board[i][j] != 0):
					row[idx] = board[i][j]
					idx += 1
			for j in range(C):
				board[i][j] = row[j]

if M[1] == 'U':
	for x in range(M[0]):
		removeZeroes(M[1])
		for j in range(C):
			for i in range(R-1):
				if(board[i][j] == board[i+1][j]):
					board[i][j] = board[i][j] << 1
					board[i+1][j] = 0
					i += 1
elif M[1] == 'D':
	for x in range(M[0]):
		removeZeroes(M[1])
		for j in range(C):
			for i in range(R-1):
				if(board[R-i-1][j] == board[R-i-1-1][j]):
					board[R-i-1][j] = board[R-i-1][j] << 1
					board[R-i-1-1][j] = 0
					i += 1
elif M[1] == 'R':
	for x in range(M[0]):
		removeZeroes(M[1])
		for i in range(R):
			for j in range(C-1):
				if(board[i][C-j-1] == board[i][C-j-1-1]):
					board[i][C-j-1] = board[i][C-j-1] << 1
					board[i][C-j-1-1] = 0
					j += 1
elif M[1] == 'L':
	for x in range(M[0]):
		removeZeroes(M[1])
		for i in range(R):
			for j in range(C-1):
				if(board[i][j] == board[i][j+1]):
					board[i][j] = board[i][j] << 1
					board[i][j+1] = 0
					j += 1

removeZeroes(M[1])
for i in range(R):
	print(' '.join(list(map(str, board[i]))))
