gameboard = [['-','-','-','-','-','-','-','-','-'], 
	['|','1','|','|','2','|','|','3','|'],
	['-','-','-','-','-','-','-','-','-'],  
	['|','4','|','|','5','|','|','6','|'],
	['-','-','-','-','-','-','-','-','-'],  
	['|','7','|','|','8','|','|','9','|'],
	['-','-','-','-','-','-','-','-','-']]

game = [[0,0,0],
	[0,0,0],
	[0,0,0]]

gameboardbTogameMapping = {'1,1' : '0,0'
	, '1,4' : '0,1'
	, '1,7' : '0,2'
	, '3,1' : '1,0'
	, '3,4' : '1,1'
	, '3,7' : '1,2'
	, '5,1' : '2,0'
	, '5,4' : '2,1'
	, '5,7' : '2,2'}

def askplayer(player):
	a = input('where do you want to go? ')
	x = int(a[0])
	y = int(a[2])
	
	
	while game[x][y] != 0:
		a = input('spot already taken! try again ')
		x = int(a[0])
		y = int(a[2])
		
	else:
		x = int(a[0])
		y = int(a[2])
		game[x][y] = player
			
def printGame():
	x = 0
	y = 0

	while x < 7:
		while y < 9:
			value = gameboardbTogameMapping.get(str(x)+','+str(y))
		
			if value != None:
				xcoord = int(value[0])
				ycoord = int(value[2])
				print(game[xcoord][ycoord], end = '')
			else:
				print(gameboard[x][y], end = '')
			y += 1
		print('')
		x += 1
		y = 0
			
def checkhorizontal(a):
	#at the current row, check if all columns match the current row column combination
	list1 = []
	row = 0
	col = 0
	while row < 3:
		while col < 3:
			list1.append(a[row][col])
			col += 1
		checklist =len(set(list1))	
		if checklist == 1:
			if list(list1)[0] != 0:
				return list(list1)[0]
	
		col = 0
		row += 1
		list1 = []
	return -1

def checkvertical(a):
	#at the current column, check if all rows match the current row column combination

	list1 = []
	row = 0
	col = 0
	while col < 3:
		while row < 3:
			list1.append(a[row][col])
			row += 1
		checklist =len(set(list1))	
		if checklist == 1:
			if list(list1)[0] != 0:
				return list(list1)[0]
	
		row = 0
		col += 1
		list1 = []
	return -1

def checkdiagonal1(a):
	#check if the row column coords match each other diagonal to the right

	list1 = []
	row = 0
	col = 0
	while col < 3:
		while row < 3:
			list1.append(a[row][col])
			row += 1
			col += 1
		checklist =len(set(list1))	
		if checklist == 1:
			if list(list1)[0] != 0:
				return list(list1)[0]
	return -1
		


def checkdiagonal2(a):
	#check if the row column coords match each other diagonal to the left

	list1 = []
	row = 0
	col = 2
	while col >= 0:
		while row < 3:
			list1.append(a[row][col])
			row += 1
			col -= 1
		checklist =len(set(list1))	
		if checklist == 1:
			if list(list1)[0] != 0:
				return list(list1)[0]
	return -1


def checkandextractwinner(a):
	horizreturn = checkhorizontal(a)
	vertreturn = checkvertical(a)
	diag1return = checkdiagonal1(a)
	diag2return = checkdiagonal2(a)

	if horizreturn != -1:
		return horizreturn
	if vertreturn != -1:
		return vertreturn
	if diag1return != -1:
		return diag1return
	if diag2return != -1:
		return diag2return





def playgame(a):

	check = 0
	
	while check < 9:
		askplayer(1)
		printGame()
		winner = checkandextractwinner(a)
		if winner != None:
			print('player ' + str(winner) + ' wins!')
			break
		check += 1
		askplayer(2)
		printGame()
		winner = checkandextractwinner(a)
		if winner != None:
			print('player ' + str(winner) + ' wins!')
			break
		check += 1
	else:
		print("no more moves")



playgame(game)


