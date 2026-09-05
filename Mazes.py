clear()
plant(Entities.Bush)
amount = get_world_size()
use_item(Items.Weird_Substance, amount)

# Clockwise Directions
Directions = [North, East, South, West]
Forward = East
index = -1

while True:

	# follow the wall currently as if east is forward direction

	# harvest if treasure found
	if get_entity_type() == Entities.Treasure:
		harvest()

	else:
		# Maze Solver: wall follow algorithm

		# Always Turn Right
		# if cannot Move Forward
		# if cannot move Left
		# if cannot Turn around


		#Foward = East
		#Directionp[1] = East
		#so left = Direction[-1] = North
		#so right = Direction[+1] = South
		## looped array so either + or - 2 works
		#so TurnAround = Direction [+-2] = West

		# find index of current Forward Direction
		for i in range(len(Directions)):
			if Directions[i] == Forward:
				index = i

		Right = Directions[(index + 1) % 4]
		# index + 3: same as -1 and stops errors
		Left = Directions[(index + 3) % 4]
		Backward = Directions[(index + 2) % 4]

		# Always Turn Right if possible
		if can_move(Right):
			move(Right)
			# update orientation
			Forward = Right

		# if cannot move Right, Try Forward
		elif can_move(Forward):
			move(Forward)
			# update orientation
			Forward = Forward

		# if cannot move Right or Forward. Try Left
		elif can_move(Left):
			move(Left)
			# update orientation
			Forward = Left

		# Cannot Move, Right,Left,Foward.
		else:
			# Turn Around
			move(Backward)
			# update orientation
			Foward = Backward
