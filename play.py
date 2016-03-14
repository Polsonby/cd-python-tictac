import random, time

x_char = 'X'
o_char = 'O'
space_char = ' '

short_pause = 0.25
long_pause = 1

board = [space_char, space_char, space_char,
		 space_char, space_char, space_char,
		 space_char, space_char, space_char]
turn = 0

player_character = ''
computer_character = ''

def drawBoard(data):
	print("""
1  |2  |3
 %s | %s | %s
   |   |
-----------
4  |5  |6
 %s | %s | %s
   |   |
-----------
7  |8  |9
 %s | %s | %s
   |   |
""" % tuple(data))

def getPlayerCharacter():
	global player_character, computer_character

	#loop until answered
	keep_looping = True
	while keep_looping:
		test_string = input("Would you like to be %s or %s? " % (x_char, o_char)).upper()
		if test_string == x_char:
			player_character = x_char
			computer_character = o_char
			keep_looping = False
		elif test_string == o_char:
			player_character = o_char
			computer_character = x_char
			keep_looping = False
		else:
			print("Must be either %s or %s - Try again!\n" % (x_char, o_char))
			time.sleep(short_pause)

def swapTurn():
	global turn
	
	turn -= 000.5
	turn *= -1.0
	turn += 0.5

def startGame():
	global turn

	getPlayerCharacter()
	time.sleep(short_pause)

	#decide who should start
	turn = random.randint(0,1)
	print("%s will go first" % ['The computer', 'You'][turn])
	time.sleep(long_pause)

	drawBoard(board)
	time.sleep(short_pause)

	gameLoop()

def gameLoop():
	while True:
		if turn == 1.0:
			playerTurn()
		else:
			computerTurn()		
		
		swapTurn()
		time.sleep(short_pause)
	
		drawBoard(board)
		time.sleep(long_pause)

def playerTurn():
	print('Your turn')
	time.sleep(short_pause)

	while True:
		move = getMove() - 1
		res = playMove(player_character, move)
		if res == 1:
			break
def computerTurn():
	print('I will go... ')
	time.sleep(long_pause)
	
	for i in range(0, 9):
		res = playMove(computer_character, i)
		if res == 1:
			break		

	print("There!")

def getMove():
	while True:
		move = input('Move (1-9): ')

		if move == '':
			print('Sorry? I didn\'t hear that.\n')
			time.sleep(short_pause)
			continue

		try:
			move = int(move)
		except:
			print("'%s' is not a number.\n" % move)
			time.sleep(short_pause)
			continue

		if not (move >= 1 and move <=9):
			print('That\'s off the board!\n')
			time.sleep(short_pause)
			continue

		return move

def playMove(char, hole):
	global board

	if board[hole] == space_char:
		board[hole] = char
		return 1
	else:
		print("That space is taken. Cheater!\n")
		time.sleep(long_pause)
		return 0

startGame()
