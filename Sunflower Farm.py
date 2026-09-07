def move_to_pos(x,y):
    # get current pos x pos y
    # input = target x,y

    # find difference
    pass

def add_flower_info(sunflowers):
    x = get_pos_x()
    y = get_pos_y()
    val = measure()
    flower = [val, x, y]
    sunflowers.append(flower)

def Initial_Plant(sunflowers):

    for _ in range(get_world_size()):
        for _ in range(get_world_size()):

            if get_ground_type() == Grounds.Grassland:
                till()
            
            plant(Entities.Sunflower)
            add_flower_info(sunflowers)

            move(North)
        move(East)



clear()
set_world_size(6)


sunflowers = []
Initial_Plant(sunflowers)
print(sunflowers)
# max uses first value in list, so val is first
print(max(sunflowers)) #[15,5,3] [val,x,y]