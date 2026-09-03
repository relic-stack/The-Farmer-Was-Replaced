clear()

while True:
	
	# loops i from (0,5) inclusive, 
	for i in range(get_world_size()):
		
		# if pos x is odd then add 1 to step counter
		if get_pos_x() % 2 != 0:
			i = i + 1
			
		# if ground not tree and taken 2 steps, plant tree
		if get_entity_type() != Entities.Tree:
			if i % 2 == 0:
				plant(Entities.Tree)
				
		# harvest if possible and if taken 2 steps plant tree
		if can_harvest() and i % 2 == 0:
			harvest()
			plant(Entities.Tree)

				
		# water only tree, if water level < 0.4
		if get_water() < 0.8 and get_entity_type() == Entities.Tree:
			use_item(Items.Water)
			
		# 1 step north
		move(North)
	move(East)
	
	
	#if get_pos_x() % 2 != 0:
		#print("Odd Row")
	#else:
		#print("Even Row")


			
