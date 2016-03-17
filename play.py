x_char = 'X'
o_char = 'O'
space_char = ' '

board = [space_char, space_char, space_char,
		 space_char, space_char, space_char,
		 space_char, space_char, space_char]
player_character = ''

def drawBoard(data):
	print("""
   |   |   
 %s | %s | %s  
   |   |
-----------
   |   |   
 %s | %s | %s
   |   |   
-----------
   |   |
 %s | %s | %s 
   |   |
""" % tuple(data))

def getPlayerCharacter():
	global player_character

	# loop forever
	keep_looping = True
	while keep_looping:
		test_string = input("Would you like to be %s or %s? " % (x_char, o_char))
		if test_string == x_char or test_string == o_char:
			player_character = test_string
			keep_looping = False
		else:
			print("Sorry but this must be either %s or %s - Try again!" % (x_char, o_char))

print("NOUGHTS")

getPlayerCharacter()
print(player_character)

drawBoard(board)
