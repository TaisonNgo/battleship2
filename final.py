# this is a battle ship game,  

# start with a grid of 3 x 3 and just one tiny ship, dingy

#  1  2  3
#a
#b    d
#c


# they have to guess the dingy is in b2

# 1 Player
# 2 Player

# place boat
# placeBoatRan = Randomizer List = A1 to J10

playnum = input("1 or 2 Player (Type 1 or 2): ")

if playnum == "1":
	# Work in Progress
	# Computer AI

	import random
	# Letter
	let = random.randint(1,10)

	print (let)

	if let == 1:
	    ltr = "a"

	if let == 2:
	    ltr = "b"

	if let == 3:
	    ltr = "c"

	if let == 4:
	    ltr = "d"

	if let == 5:
	    ltr = "e"

	if let == 6:
	    ltr = "f"

	if let == 7:
	    ltr = "g"

	if let == 8:
	    ltr = "h"

	if let == 9:
	    ltr = "i"

	if let == 10:
	    ltr = "j"

	num = random.randint(1,10)
	# Number
	print (num)

	if num == 1:
	    nmr = "1"

	if num == 2:
	    nmr = "2"

	if num == 3:
	    nmr = "3"

	if num == 4:
	    nmr = "4"

	if num == 5:
	    nmr = "5"

	if num == 6:
	    nmr = "6"

	if num == 7:
	    nmr = "7"

	if num == 8:
	    nmr = "8"

	if num == 9:
	    nmr = "9"

	if num == 10:
	    nmr = "10"

	loce = ltr + nmr

	print (loce)

	while True:
		player = input("Where's the dingy located? Ex: b2: ")
		if player == loce:
			print ("You blew up the dingy")
			break
		else:
			print ("Miss")

elif playnum == "2":
	# place boat
	placeBoatp1 = input("Where do you want to place your boat? (P1) Ex: a1: ")
	placeBoatp2 = input("Where do you want to place your boat? (P2) Ex: a1: ")
	# guess boat placement
	while True:
		humanGuessp1 = input("Where's the dingy located? (P1) Ex: a1: ")
		if (humanGuessp1 == placeBoatp2):
			print ("You found the dingy")
			print ("Player 1 Wins")
			break
		else:
			print("Miss")
	#player2 Guess
		humanGuessp2 = input("Where's the dingy located? (P2) Ex: a1: ")
		if (humanGuessp2 == placeBoatp1):
			print ("You found the dingy")
			print ("Player 2 Wins")
			break
		else:
			print("Miss")

else:
	print ("Type 1 or 2")

while True:
	button = input("The End")

# stop
