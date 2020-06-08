from tabulate import tabulate
import numpy as np

class Player(object):
	"""
	Three attributes:
		Name
		Piece (X or O)
		Score
	"""

	def __init__(self, n, p, s):
		self.name = n
		self.piece = p
		self.score = s

class Board(object):
	"""docstring for Board"""
	def __init__(self, arg):
		board = []

		for i in range(arg):
			row = []
			for j in range(arg):
				row.append('-')
			board.append(row)
		self.board = board
		self.board_size = arg
	
	# def __init__(self, arg):
	# 	board = PrettyTable([i for i in range(arg)])
	# 	for i in range(arg):
	# 		board.add_row([None for j in range(arg)])

	# 	self.board = board

	def displayBoard(self):
		print(tabulate(self.board, headers=[i for i in range(self.board_size)]))

	def changeSpace(self, row, col, piece):
		if self.board[row][col] == '-':
			self.board[row][col] = piece
			return 1

		else:
			return None

	def checkRows(self):

		for row in self.board:
			if len(set(row)) == 1:
				print("Row")
				return row[0]
		return 0

	def checkDiag(self):

		if (len(set([self.board[i][i] for i in range(self.board_size)]))) == 1:
			print("Diag1")
			return self.board[0][0]

		if (len(set([self.board[i][self.board_size-i-1] for i in range(self.board_size)]))) == 1:
			print("Diag2")
			return self.board[0][self.board_size-1]
		return 0

	def checkWin(self):

		for newBoard in [self.board, np.transpose(self.board)]:
			newBoard = Board(len(newBoard))
			result = newBoard.checkRows()
			if result:
				return result

		return checkDiag(self.board)