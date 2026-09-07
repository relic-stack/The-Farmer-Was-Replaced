def move_to_pos(target_x, target_y):
	current_x = get_pos_x()
	current_y = get_pos_y()

	# Find Difference Between Points
	x_diff = target_x - current_x
	y_diff = target_y - current_y

	if x_diff >= 0:
		for _ in range(x_diff):
			move(East)
	else:
		for _ in range(abs(x_diff)):
			move(West)

	if y_diff >= 0:
		for _ in range(y_diff):
			move(North)
	else:
		for _ in range(abs(y_diff)):
			move(South)



def add_flower_info(sunflowers):
	x = get_pos_x()
	y = get_pos_y()
	val = measure()
	flower = [val, x, y]
	sunflowers.append(flower)


def max_flower(sunflowers):
	max_flower = None
	max_val = -1

	for flower in sunflowers:
		if flower[0] > max_val:
			max_val = flower[0]
			max_flower = flower

	return max_flower

def Initial_Plant(sunflowers):

	for _ in range(get_world_size()):
		for _ in range(get_world_size()):

			if get_ground_type() == Grounds.Grassland:
				till()

			use_item(Items.Water)
			plant(Entities.Sunflower)
			add_flower_info(sunflowers)

			move(North)
		move(East)



clear()
#set_world_size(3)



sunflowers = []
sunflower_values = []
Initial_Plant(sunflowers)

# max uses first value in list, so val is first
# max(sunflowers)) #[15,5,3] [val,x,y]

Target = max_flower(sunflowers)
x = Target[1] # type: ignore
y = Target[2] # type: ignore
move_to_pos(x,y)



while True:


	Target = max_flower(sunflowers)
	x = Target[1] # type: ignore
	y = Target[2] # type: ignore
	move_to_pos(x,y)

	if can_harvest():
		harvest()
		# remove flower from list
		sunflowers.remove(Target)
		plant(Entities.Sunflower)
		# add flower to list
		add_flower_info(sunflowers)
		Target = max_flower(sunflowers)
		x = Target[1] # type: ignore
		y = Target[2] # type: ignore

