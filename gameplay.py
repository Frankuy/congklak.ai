#****************************************************
# Put all constants below
#****************************************************
NUMBER_OF_HOLES = 7

#****************************************************
# Put all global variables below
#****************************************************
holes_player = []
holes_opponent = []
house_player = 0
house_opponent = 0
temp_seed = 0
turn = 0

#****************************************************
# Fill each hole with a certain number of seed
#****************************************************
def fill_holes(holes, seed):
    for i in range(NUMBER_OF_HOLES):
        holes.append(seed)

#****************************************************
# Take all seeds in a hole
# and put them into temporary
#****************************************************
def take_all_seeds(index, holes, seed):
    seed = holes[index]
    holes[index] = 0

#****************************************************
# Add a seed into hole
#****************************************************
def add_seed_to_hole(index, holes, seed):
    holes[index] += 1
    seed -= 1

#****************************************************
# Add a seed into hole
#****************************************************
def add_seed_to_house(house, seed):
    house += 1
    seed -= 1

#****************************************************
# Stop seed movement
#****************************************************
def stop_seed_movement(play_condition, seed, last_position, last_idx, holes_player, holes_opponent):
    if (last_position == 'house' and seed == 0)
    or (last_position == 'holes_player' and holes_player[last_idx] == 1)
    or (last_position == 'holes_opponent' and holes_opponent[last_idx] == 1):
        play_condition = False


#****************************************************
# Move seed clockwise and stop based on the rules
#****************************************************
def move_seeds(turn, index, holes_player, holes_opponent, house_player, seed):
    take_all_seeds(index, holes_player, seed)
    play_condition = True
    start_idx = index+1
    last_idx = start_idx
    last_position = 'holes_player'

    while play_condition:
        for i in range(start_idx, NUMBER_OF_HOLES):!
            add_seed_to_hole(i, holes_player, seed)
            last_idx = i
            last_position = 'holes_player'
            stop_seed_movement(play_condition, seed, last_position, last_idx, holes_player, holes_opponent)
            if not(play_condition):
                break
        start_idx = 0

        add_seed_to_house(house_player, seed)
        last_position = 'house'
        stop_seed_movement(play_condition, seed, last_position, last_idx, holes_player, holes_opponent)

        for i in range(NUMBER_OF_HOLES):
            add_seed_to_hole(i, holes_opponent, seed)
            last_idx = i
            last_position = 'holes_opponent'
            stop_seed_movement(play_condition, seed, last_position, last_idx, holes_player, holes_opponent)
            if not(play_condition):
                break

    if last_position == 'holes_player' and holes_opponent[NUMBER_OF_HOLES-last_idx-1] != 0:
        house_player += (holes_player[last_idx] + holes_opponent[NUMBER_OF_HOLES-last_idx-1])
        holes_player[last_idx] = 0
        holes_opponent[NUMBER_OF_HOLES-last_idx-1] = 0