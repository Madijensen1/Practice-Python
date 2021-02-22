import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#checks the value of a card
def check_value(player):

		cardlength = len(player.allcards)
		handsum = 0

		for x in range(cardlength):
			handsum = handsum + player.allcards[x].value

		return handsum

#creates a card with a rank, suit, and value attached
class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]


	def __str__(self):
		return self.rank + ' of ' + self.suit

#creates a deck of 52 cards using the Card class
class Deck:
	
	def __init__(self):
		
		self.allcards = []

		for suit in suits:
			for rank in ranks:
				createcard = Card(suit,rank)
				self.allcards.append(createcard)

	def shuffle(self):
		random.shuffle(self.allcards)

	def dealone(self):
		return self.allcards.pop()

#sets up the player hand, creates ability to add cards to the hand and check the value
class Player:

	def __init__(self):
		self.allcards = []
	
	def addcard(self, newcard):
		self.allcards.append(newcard)
	
	@property
	def handVal(self):
		return check_value(self)

	def __str__(self):
		return f"human has {len(self.allcards)} cards."

#creates the dealers hand, creates ability to add cards to the hand and check the value
class Dealer:

	def __init__(self):
		self.allcards = []
	
	def addcard(self, newcard):
		self.allcards.append(newcard)
	
	@property
	def handVal(self):
		return check_value(self)

	def __str__(self):
		return f"dealer has {len(self.allcards)} cards."


class Blackjack:

	def __init__(self):
		self.dealerwin = 0
		self.humanwin = 0

	def gamesetup(self):
		self.human = Player()
		self.dealer = Dealer()

		self.usedeck = Deck()
		self.usedeck.shuffle()

		for x in range(2):
			self.human.addcard(self.usedeck.dealone())
			self.dealer.addcard(self.usedeck.dealone())

	#prints game without values added (like a true blackjack game, you can't see the value)
	def printgame(self):
		
		humanlist = ""
		firstRun = True
		for x in self.human.allcards:
			if not firstRun:
				humanlist += ', '
			humanlist = humanlist + str(x)
			firstRun = False
	
		return 'dealer hand: ' + str(self.dealer.allcards[0]) + ", one hidden \nhuman hand: "+ humanlist
	
	#prints game with values, easier to compare dealer vs player hand
	def fullprintgame(self):
		
		humanlist = ""
		for x in self.human.allcards:
			humanlist = humanlist + str(x) + ', '
		
		dealerlist = ""
		for x in self.dealer.allcards:
			dealerlist = dealerlist + str(x) + ', '
		
	
		return 'dealer hand: ' + dealerlist + "dealer hand = " + str(self.dealer.handVal) + "\nhuman hand: "+ humanlist + "human hand = " + str(self.human.handVal)

	#checks if the player has an ace, resets the value based on input
	def aceplayer(self):
		for rank in ranks:
			if rank == 'Ace':
				for x in self.human.allcards:
					if rank == x.rank:
						print(self.printgame())
						try:
							acenum = int(input('you have an ' + str(x) + '! is it worth 1 or 11? '))
							if acenum == 1:
								x.value = 1
						except:
							print('not 1 or 11! try again ')

	#checks if the player has gone bust
	def checkbust(self,playerdealer):
		if playerdealer.handVal > 21:
			return False
				
		else:
			return True

	#creates the loop of the players turn, adding a card to the hand if "hit", checking if bust and if they have an ace
	def player_turn(self):

		not_busted = True

		while not_busted:
			print(self.printgame())	

			turn = input('hit or pass? ')
			
			if turn == 'hit':
				self.human.addcard(self.usedeck.dealone())
				self.aceplayer()

				if self.human.handVal > 21:
					not_busted = False
				
			if turn == 'pass':
				not_busted = False
			
			while 'hit' != turn != 'pass':
				turn = input('Not right! pick one - hit or pass? ')
	
	#creates the dealers turn based on traditional dealer rules
	def dealer_turn(self):

		not_bust = True

		while not_bust:
			while self.dealer.handVal <= 21:
				if self.dealer.handVal not in range(17,22):
					self.dealer.addcard(self.usedeck.dealone())
				
				if self.dealer.handVal in range(17,22):
					break
				
				if self.dealer.handVal > 22:
					not_bust = False

			if not_bust == False:

				for rank in ranks:
					if rank == 'Ace':
						for x in self.dealer.allcards:
							if rank in str(x):
								if x.rank == 'Ace':
									x.value = 1
									not_bust = True
			else:
				break
	#function to check and return who wins
	def who_win(self):

		if self.checkbust(self.human) == False:
			if self.dealer.handVal < 21:
				print('human bust, dealer wins!')
				return 'dealer'

		if self.human.handVal <= 21 and self.dealer.handVal <= 21:
			if self.human.handVal > self.dealer.handVal:
				print('human wins!')
				return 'human'

			if self.human.handVal < self.dealer.handVal:
				print('dealer wins!')
				return 'dealer'

			if self.human.handVal == self.dealer.handVal:
				print('its a tie')
				return 'tie'
		
		if self.human.handVal > 21 and self.dealer.handVal > 21:
			print('dealer and human bust')
		
		if self.human.handVal <= 21 and self.dealer.handVal > 21:
			print('dealer bust, human wins!')
			return 'human'

		#return win counts
	def wincount(self,winner):
	
		if winner == 'dealer':
			self.dealerwin += 1
		
		if winner == 'human':
			self.humanwin += 1
		print('game score: dealer - ' + str(self.dealerwin) + ' human - ' + str(self.humanwin))

#creates betting system where you can place a bet before the round starts, then will divide the bet based on who won the last round
class Betting():

	def __init__(self,balance = 0,table = 0):
		self.balance = balance
		self.table = table

	def makebet(self):
		bet = 0
		while bet == 0:
			try:
				bet = int(input('place a bet? you have $' + str(self.balance) + ' - $'))
				if bet < 0:
					print('no negatives please')
					bet = 0
				if bet > self.balance:
					print('funds not available')
					bet = 0
			except:
				print('not a number! try again')
				bet = 0
		
		self.balance = self.balance - bet
		self.table = self.table + bet*2

	def dividebet(self,winner):
		if winner == 'human':
			self.balance = self.balance + self.table
			print('you win! $' + str(self.table) + ' has been added to your wallet. total - $' + str(self.balance))
		
		if winner == 'tie':
			self.balance = self.balance + (self.table/2)
			print('your bet - $' + str(int(self.table)) + ' has been added back to your wallet. total - $' + str(self.balance))
		
		self.table = 0
	

	def __str__(self):
		return 'wallet total: $' + str(self.balance)

#checks if player wants to continue with current game
def playagain(gamebet):
	if gamebet.balance == 0:
		print('no funds left, game over')
		return False

	ask = input('play again? yes or no - ')
	if ask == 'yes':
		return True
	else:
		return False

#sets up entire game to be played from command line
def playblackjack():
	play = True
	game = Blackjack()
	gamebet = Betting(100,0)
	print('This is simple blackjack! play against the dealer. you can place a bet then hit or pass')
	
	while play:
		game.gamesetup()
		print(gamebet)
		gamebet.makebet()
		game.player_turn()
		game.dealer_turn()
		winner = game.who_win()
		print(game.fullprintgame())
		game.wincount(winner)
		gamebet.dividebet(winner)
		print(gamebet)
		play = playagain(gamebet)

playblackjack()
