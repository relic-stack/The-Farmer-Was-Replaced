clear()

while True:

	for i in range(get_world_size()):

		use_item(Items.Fertilizer)

		if can_harvest():
			harvest()

		move(North)
	move(East)