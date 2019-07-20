# Rock,Paper,Scissor
# AUTHOR: RICHARD BARTLEWITZ
# This script will randomy select rock, paper, or scissor to play the game with the user

import random

# initialize the while loop
keep_play = str("y")

# keeps game going
while keep_play == str("y"):
	comp_selection = random.randint(0,2)
#	print(comp_selection)                        # prints the computers selection before user makes their move

	# ask user to make their move
	user_selection = str(input("\n" + "To Play Type Your Guess: rock, paper, or scissor: "))

	# user_selection translation data type
	if user_selection == "rock":
		number_user = int(0)
	elif user_selection == "paper":
		number_user = int(1)
	elif user_selection == "scissor":
		number_user = int(2) 
	else:
		while user_selection != str("rock") and user_selection != str("paper") and user_selection != str("scissor"):
			user_selection = str(input("\n" + "Please type one of the following: rock, paper, or scissor: "))


	# GAME MECHANICS
	if number_user == comp_selection:
		print("\n" + "Tie! Lets play again")
		
	elif number_user == 0 and comp_selection == 2:
		print("\n" + "You Win!")

	elif number_user == 0 and comp_selection == 1:
		print("\n" + "You Lose!")

	elif number_user == 1 and comp_selection == 0:
		print("\n" + "You Win!")

	elif number_user == 1 and comp_selection == 2:
		print("\n" + "You Lose!")

	elif number_user == 2 and comp_selection == 1:
		print("\n" + "You Win!")

	elif number_user == 2 and comp_selection == 0:
		print("\n" + "You Lose!")

	keep_play = str(input("\n" + "If you would like to play again press y if not press any other key: " + "\n"))