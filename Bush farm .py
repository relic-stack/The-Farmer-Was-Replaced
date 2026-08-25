clear()
	
while True:
	
	for i in range(get_world_size()):
		if get_entity_type() != Entities.Bush:
			plant(Entities.Bush)
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			
		move(North)
	move(East)
	

		