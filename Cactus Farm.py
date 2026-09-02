clear()
change_hat(Hats.Cactus_Hat)

def plant_crop(crop):

	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(crop)
			move(North)
		move(East)


plant_crop(Entities.Cactus)


def move_done(direction,n):
	for i in range(n):
		move(direction)

# sort using bubble sort

# sort row 1

n = get_world_size()
# loop through row

for i in range(n):
	swapped = False

	# bubble sort inner loop
	for j in range(0, n-i-1): # try 0, n - i -1

		# check we have cactus, always return integers
		if get_entity_type() == Entities.Cactus:
			# measure crop and crop to the east
			x = measure()
			y = measure(East)

		# if current is bigger, swap cactus
		if x > y: # type: ignore
			# swap
			swap(East)
			swapped = True
		move(East)


	# move east i times (reset back to start of row)
	# i+1 due to i starting at 0
	move_done(East, i+1)

	# if sorted stop
	if swapped == False:
		break

# sort columns
