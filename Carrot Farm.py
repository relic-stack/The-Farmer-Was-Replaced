clear()

NorthCount = 0
while True:
	
	if NorthCount == get_world_size():
		move(East)
		NorthCount = 0
		
			
	if can_harvest():
		harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)
		if get_water() < 0.6:
			use_item(Items.Water)

	if get_entity_type() != Entities.Carrot:
			till()
			plant(Entities.Carrot)
		


	move(North)
	NorthCount += 1
	


			
		