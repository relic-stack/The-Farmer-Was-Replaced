plant(Entities.Bush)
amount = get_world_size()
use_item(Items.Weird_Substance, amount)


Forward = East

while True:

    # follow the wall currently as if east is forward direction

    # harvest if treasure found
    if get_entity_type() == Entities.Treasure:
        harvest()

    else:
        # dead end condition
        if can_move(North) == False and can_move(East) == False and can_move(South) == False:
            # Turn around, set direction to opposite e,g +180deg
            move(South)
            # since turn around, swap around direction as opposite direction

        # T junction condition, always turn right
        if can_move(East) == False:
            move(South)

        # right corner condition, always turn right
        if can_move(North) == False and can_move(East) == False:
            move(South)


        # left corner condition, always turn left
        if can_move(South) == False and can_move(East) == False:
            move(North)

        # straight line condition, continue forward
        if can_move(South) == False:
            move(East)