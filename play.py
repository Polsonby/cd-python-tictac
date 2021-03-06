import random
game_in_progress = True
x_char = 'X'
o_char = 'O'
space_char = ' '

board = [space_char, space_char, space_char,
		 space_char, space_char, space_char,
		 space_char, space_char, space_char]

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

def validMove(move):
	if move > 8:
		return False
	elif move < 0:
		return False
	elif not boxFree(move):
		return False
	else:
		return True

def getPlayerMove():
	while True:
		try:
			choice = int(input("Where would you like to go? "))
			choice -= 1
		except ValueError:
			print("This number must be an integer!")
			continue
		
		if choice > 8:
			print ("This is too high")
		elif choice < 0:
			print ("This is too low")
		elif not boxFree(choice):
			print ("This space has already been taken!")
		else:
			break
	writePosition(player_character, choice);

def calculateComputerMove():
	while True:
		choice = random.randint(1, 9) - 1
		
		if validMove(choice):
			break
	
	writePosition(computer_character, choice);

def getPlayerCharacter():
	global player_character, computer_character

	# loop forever
	keep_looping = True
	while keep_looping:
		test_string = input("Would you like to be %s or %s? " % (x_char, o_char)).upper()
		if test_string == x_char or test_string == o_char:
			player_character = test_string
			computer_character = o_char if player_character == x_char else x_char
			keep_looping = False
		else:
			print("Sorry but this must be either %s or %s - Try again!" % (x_char, o_char))

def boxFree(move):
	if board[move] == space_char:
		return True
	else:
		return	False 
		
def writePosition(user_character, position):
	board[position] = user_character

print("Naughts and Crosses\n")

getPlayerCharacter()
print(player_character)

def isWinner(char):
	return (board[0] == char and board[1] == char and board[2] == char) or (board[0] == char and board[4] == char and board[8] == char) or (board[0] == char and board[3] == char and board[6] == char) or (board[1] == char and board[4] == char and board[7] == char) or (board[2] == char and board[4] == char and board[6] == char) or (board[2] == char and board[5] == char and board[8] == char)or (board[3] == char and board[4] == char and board[5] == char)or (board[6] == char and board[7] == char and board[8] == char)
def getGameStatus():
	#print("Game won" if isWinner('X') or isWinner('O') else "Game still playing")
	if isWinner('X'):
		return 1
	elif isWinner("O"):
		return 2
	else:
		return 0
def printStatusMessage(status):
	if status == 1:
		print ("x won!")
	elif status == 2:
		print ("O won")


		
while game_in_progress == True:
	drawBoard(board)
	getPlayerMove()
	calculateComputerMove()
	status = getGameStatus()
	printStatusMessage(status)


