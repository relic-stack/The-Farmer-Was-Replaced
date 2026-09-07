# max 2 drones currently
clear()
print(max_drones())

# quicker carrot farm

# Farm Function for any Direction e.g Rows or Cols
def Farm(D1, D2):
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
			
            if get_ground_type() != Grounds.Soil:
                till()
                use_item(Items.Water)
                plant(Entities.Carrot)

            if can_harvest():
                harvest()
                use_item(Items.Water)
                plant(Entities.Carrot)

            move(D1)
        move(D2)

            
def go_top_right_world(x,y):
	for _ in range(x):
		move(East)
	for _ in range(y):
		move(North)


def drone_task():
    n = get_world_size()
    go_top_right_world(n-1,n-1)
    while True:
        Farm(South, West)


if num_drones() < max_drones():
    spawn_drone(drone_task)

do_a_flip()
while True:
    Farm(North, East)
        
		
