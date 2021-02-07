def randomword():
	import random
	wordlist = []
	wordsplit = []

	with open('sowpods.txt', 'r') as f:
  		word = f.readlines()
	
	for x in word:
		wordlist.append(x.strip())	

	randnum = random.randint(0, len(wordlist))

	guessword = wordlist[randnum].lower()
	
	for x in guessword:
		wordsplit.append(x)

	return wordsplit

def gameboard(a):

	gameboard = []

	#print gameboard for how many letters in the word
	for letter in a:
		gameboard.append('-')
	return gameboard
	
def printgame(gamehere):
	for underscore in gamehere:
		print(underscore, end = '')
	print('')
	
	
def guessing(thisword,game,used):

	
	#write the logic that asks a player to guess a letter
	guess = input('give me a letter ').lower()
	while guess in used:
		guess = input('already guessed! give me another letter ').lower()
	used.append(guess)

# displays letters in the clue word that were guessed correctly.
	
	characters = len(thisword)
	count = 0
	changes = 0
	while count < characters:
		if thisword[count] == guess:
			game[count] = guess
			changes += 1
		count += 1
	
	if changes != 0:
		return True
	else:
		return False
		


def win(game):
	if '-' not in game:
		return True
		

	else:
		return False
	

buildinglist = [' _______',
	'|   |',
	'|',
	'|   o',
	'|   |',
	'|  /|',
	"|  /|\ ",
	"|  /",
	"|  / \ "]

def emptyboard(buildinglist):
	print(buildinglist[0])
	print(buildinglist[1])
	print(buildinglist[2])
	print(buildinglist[2])
	print(buildinglist[2])


def turnone(buildinglist):
	print(buildinglist[0])
	print(buildinglist[1])
	print(buildinglist[3])
	print(buildinglist[2])
	print(buildinglist[2])

def turntwo(buildinglist):
	print(buildinglist[0])
	print(buildinglist[1])
	print(buildinglist[3])
	print(buildinglist[4])
	print(buildinglist[2])

def turnthree(buildinglist):
	print(buildinglist[0])
	print(buildinglist[1])
	print(buildinglist[3])
	print(buildinglist[5])
	print(buildinglist[2])

def turnfour(buildinglist):
	print(buildinglist[0])
	print(buildinglist[1])
	print(buildinglist[3])
	print(buildinglist[6])
	print(buildinglist[2])

def turnfive(buildinglist):
	print(buildinglist[0])
	print(buildinglist[1])
	print(buildinglist[3])
	print(buildinglist[6])
	print(buildinglist[7])

def turnsix(buildinglist):
	print(buildinglist[0])
	print(buildinglist[1])
	print(buildinglist[3])
	print(buildinglist[6])
	print(buildinglist[8])

def printboard(buildinglist, remainingturns):
	if remainingturns == 6:
		emptyboard(buildinglist)
	if remainingturns == 5:
		turnone(buildinglist)
	if remainingturns == 4:
		turntwo(buildinglist)
	if remainingturns == 3:
		turnthree(buildinglist)
	if remainingturns == 2:
		turnfour(buildinglist)
	if remainingturns == 1:
		turnfive(buildinglist)
	if remainingturns == 0:
		turnsix(buildinglist)


def hangman():
	used = []
	remainingturns = 6
	currentword = randomword()
	emptygame = gameboard(currentword)

	while remainingturns > 0 and win(emptygame) != True:
		#printgame(currentword)
		printgame(emptygame)
		if guessing(currentword, emptygame, used) == False:
			remainingturns -= 1
			if remainingturns == 0:
				print('no more turns, game over :(')
				print('the answer was ' + ''.join(currentword))
			else:
				print('wrong! you have '+str(remainingturns) + ' wrong guesses left')
		printboard(buildinglist, remainingturns)

		if win(emptygame) == True:
			print('you win! the answer was ' + ''.join(currentword))
		

	
			
	
hangman()

	#stop the game when all the letters have been guessed correctly