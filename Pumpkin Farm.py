clear()
Dead_Pumpkin_Found = True
while num_items(Items.Carrot) != 0:

	for i in range(get_world_size()):

		for j in range(get_world_size()):


			if get_entity_type() != Entities.Pumpkin:

				if get_entity_type() == Entities.Dead_Pumpkin:
					Dead_Pumpkin_Found = True
					plant(Entities.Pumpkin)
				else:
					if get_ground_type() == Grounds.Grassland:
						till()
					plant(Entities.Pumpkin)

                
			if num_items(Items.Carrot) == 0:
				break
                        
			move(North)

		if num_items(Items.Carrot) == 0:
			break
            
		move(East)
	print("1 map loop complete")

	# if no dead found and can harvest then harvest
	if Dead_Pumpkin_Found == False and can_harvest():
		harvest()

    # reset Found to False 
	Dead_Pumpkin_Found = False

print("Carrot Stock is empty")
    

# Notes: Bug with harvesting first few pumpkins on grid even if
# pumpkin is not dead. Implementation needs debugging then
# cleaning up.