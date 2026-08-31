clear()

change_hat(Hats.Cactus_Hat)

North_array = []
East_array = [] 


while num_items(Items.Pumpkin) > 1:

	for i in range(3):

		for j in range(3):

			if get_ground_type() != Grounds.Soil:
				till()


			plant(Entities.Cactus)

			if can_harvest():
				harvest()

			move(North)

		move(South)
		move(South)
		move(South)
		move(East)

	move(West)
	move(West)
	move(West)

	# Implement Bubble sort as matches ingame implementation
	# bubble sort rows then columns? As apparently if sort rows first wont change order when columns sorted

	break