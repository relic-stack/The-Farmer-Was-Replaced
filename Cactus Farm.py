clear()
change_hat(Hats.Cactus_Hat)



# function to plant entire world
def plant_crop_world(crop):

	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(crop)
			move(North)
		move(East)



# function to move direction n times
def move_drone(direction,n):
	for i in range(n):
		move(direction)



# Bubble Sort Implementation in chosen direction e.g East = Row, North = Column
def bubble_sort(direction):

	n = get_world_size()

	# outer loop
	for i in range(n):
		swapped = False

		# bubble sort inner loop
		for j in range(0, n-i-1):

			# check we have cactus, always return integers
			if get_entity_type() == Entities.Cactus:
				# measure crop and crop to the east
				x = measure()
				y = measure(direction)

			# if cactus is bigger, swap cactus
			if x > y: # type: ignore
				swap(direction)
				swapped = True
			move(direction)

		# move east i+1 times (reset back to start of row)
		move_drone(direction, i+1)

		# if sorted stop
		if swapped == False:
			break



plant_crop_world(Entities.Cactus)

# bubble sort every row in world 
for i in range(get_world_size()):
	bubble_sort(East)
	move(North)

# bubble sort every column in world
for i in range(get_world_size()):
	bubble_sort(North)
	move(East)




# Notes
# next step is to put bubble sort code into function so it can run on each row
# then on each column to get full sorted grid In direction NE
