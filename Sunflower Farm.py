clear()

set_world_size(6)

def move_to_pos(x,y):
    # get current pos x pos y
    # input = target x,y

    # find difference
    pass







for i in range(get_world_size()):
    for j in range(get_world_size()):

        if can_harvest():
            harvest()

        if get_ground_type() == Grounds.Grassland:
            till()

        plant(Entities.Sunflower)
        move(North)
    move(East)