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

# sort using bubble sort

# sort row 1

n = get_world_size()
# loop through row

for i in range(n):
	swapped = False

	# bubble sort inner loop
	for j in range(0, n): # try 0, n - i -1

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

	# if sorted stop
	if swapped == False:
		break


# Debug Notes:
# inner loop j, for bubble sort when using 0, n-i-1
# Not completed sort, missing few smaller cactus
# However 0,n gets them all so need debugging
#	
#





# sort columns
