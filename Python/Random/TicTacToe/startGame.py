import classes

def takeTurn(player: classes.Player, board: classes.Board) -> None:

	viable = None
	board.displayBoard()
	print("{} please take your turn.".format(player.name))

	while (viable == None):
		row = int(input("Enter the row-coordinate for your move (ex: 0, 1, 2...): "))
		col = int(input("Enter the column-coordinate for your move (ex: 0, 1, 2...): "))
		viable = board.changeSpace(row, col, player.piece)


def main():

	board_size = int(input("How big would you like your board to be: "))

	board = classes.Board(board_size)
	board.displayBoard()
	name = input("Player 1 please enter your name: ")
	player1 = classes.Player(name, 'X', 0)

	name = input("Player 2 please enter your name: ")
	player2 = classes.Player(name, 'O', 0)

	curr_player = 1
	result = ''
	while(not result):
		if(curr_player):
			takeTurn(player1, board)
		else:
			takeTurn(player2, board)
		curr_player = not curr_player
		result = input("Press ENTER to continue, anything else to end game: ")

	if(curr_player): #Player 1 wins
		print("{} wins!".format(player1.name))
	else:
		print("{} wins!".format(player2.name))

if __name__ == '__main__':
	main()