
def Maze_Solver():
	# Clockwise Directions
	Directions = [North, East, South, West]
	# Initialise Variables
	Forward = East
	index = -1

	while True:

		# harvest if treasure found
		if get_entity_type() == Entities.Treasure:
			harvest()
			break

		else:
			# Take Step Through Maze
			# Algorithm (Wall Follower):
				# Always Turn Right
				# if cannot Move Forward
				# if cannot move Left
				# if cannot Turn around

			# find index of current Forward Direction
			for i in range(len(Directions)):
				if Directions[i] == Forward:
					index = i

			# Find Directions based on Forward (Current Orientation)
			Right = Directions[(index + 1) % 4]
			Left = Directions[(index + 3) % 4]
			Backward = Directions[(index + 2) % 4]

			# Always Turn Right if possible
			if can_move(Right):
				# Move + Update Orientation
				move(Right)
				Forward = Right

			# if cannot move Right, Try Forward
			elif can_move(Forward):
				# Move + Update Orientation
				move(Forward)
				Forward = Forward

			# if cannot move Right or Forward. Try Left
			elif can_move(Left):
				# Move + Update Orientation
				move(Left)
				Forward = Left

			# Cannot Move, Right,Left,Foward.
			else:
				# Turn Around + Update Orientation
				move(Backward)
				Forward = Backward



# Debug
set_world_size(6)



clear()
change_hat(Hats.Gold_Hat)

while True:
	plant(Entities.Bush)
	amount = get_world_size()
	use_item(Items.Weird_Substance, amount)
	Maze_Solver()

