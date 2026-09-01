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

	# if sorted stop
	if swapped == False:
		break


# Debug Notes:
# inner loop j, for bubble sort when using 0, n-i-1
# Not completed sort, missing few smaller cactus
# However 0,n gets them all so need debugging
#	
# Issue is the move(east), if we have n, we move east x1
# as at end of row its resets to start of row. However, if we stop
# at pos 11 instead of 12, we need to move east x2.
# create func to move east n times, after j loop complete, 
# move east i times?, aim to get to start of row after each inner loop







# sort columns
