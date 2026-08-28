clear()

while num_items(Items.Pumpkin) <2:

    for i in range(get_world_size()):

        for j in range(get_world_size()):

            if get_ground_type() != Grounds.Soil:
                till()


            plant(Entities.Cactus)

            if can_harvest():
                harvest()

            move(North)

        move(East)