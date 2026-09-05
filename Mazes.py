plant(Entities.Bush)
amount = get_world_size()
use_item(Items.Weird_Substance, amount)

# Clockwise Directions
Directions = [North, East, South, West]
Forward = East

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

		pass
