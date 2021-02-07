

def play1winner(play1, play2):
	if play1 == 'rock':
		if play2 == 'scissors':
			print('player 1 wins!')
			return True
	if play1 == 'paper':
		if play2 == 'rock':
			print('player 1 wins!')
			return True
	if play1 == 'scissors':
		if play2 == 'paper':
			print('player 1 wins!')
			return True
	
def play2winner(play1, play2):
	if play2 == 'rock':
		if play1 == 'scissors':
			print('player 2 wins!')
			return True
	if play2 == 'paper':
		if play1 == 'rock':
			print('player 2 wins!')
			return True
	if play2 == 'scissors':
		if play1 == 'paper':
			print('player 2 wins!')
			return True

def tie(play1, play2):
	if play1 == play2:
		print("its a tie!")


def rps():
	player1tally = 0
	player2tally = 0
	
	play1 = input("rock paper scissors! player 1 - shoot - ")
	play2 = input("rock paper scissors! player 2 - shoot - ")
	
	tie(play1, play2)
	
	if play1winner(play1, play2) == True:
		player1tally += 1

	if play2winner(play1, play2) == True:
		player2tally += 1
	
	print('score - player 1 = ' + str(player1tally) + ' player 2 = ' + str(player2tally))


def play():	
	rps()
	again = input('play again? y or n - ')
	while again == 'y':
		rps()
		again = input('play again? y or n - ')

play()