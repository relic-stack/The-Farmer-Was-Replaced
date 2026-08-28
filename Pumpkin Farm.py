clear()
Dead_Pumpkin_Found = True
while True:

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

            # water every step (Due to waiting time for big pumpkin, water not worth it)
            #if get_water() < 0.7:
                #use_item(Items.Water)

            move(North)

        move(East)
    print("1 map loop complete")

    # if no dead found and can harvest then harvest
    if Dead_Pumpkin_Found == False and can_harvest():
        harvest()

    # reset Found to False 
    Dead_Pumpkin_Found = False

# Notes: Bug with harvesting first few pumpkins on grid even if
# pumpkin is not dead. Implementation needs debugging then
# cleaning up.