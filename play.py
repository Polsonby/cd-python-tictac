player_character = ''

def getPlayerCharacter():
	global player_character

	# loop forever
	keep_looping = True
	while keep_looping:
		test_string = input("Would you like to be X or 0?")
		if test_string == "X" or test_string == "O":
			player_character = test_string
			keep_looping = False
		else:
			print("Sorry but this must be either X or O - try again!")

print("NOUGHTS")

getPlayerCharacter()
print(player_character)
