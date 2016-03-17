x_char = 'X'
o_char = 'O'
space_char = ' '

board = [space_char, o_char, space_char,
		 space_char, space_char, space_char,
		 space_char, space_char, space_char]
player_character = ''

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
	global player_character

	# loop forever
	keep_looping = True
	while keep_looping:
		test_string = input("Would you like to be %s or %s? " % (x_char, o_char)).upper()
		if test_string == x_char or test_string == o_char:
			player_character = test_string
			keep_looping = False
		else:
			print("Sorry but this must be either %s or %s - Try again!" % (x_char, o_char))

def writePosition(user_character, position):
	board[position] = user_character;

print("NOUGHTS")

getPlayerCharacter()
print(player_character)

while True:
	drawBoard(board)

	while True:
		choice = int(input("Where would like to go? "))

		if choice > 9:
			print ("this is too high")
		elif choice < 1:
			print ("this is too low")
		else:
			break
			
	choice -= 1

	writePosition('X', choice);