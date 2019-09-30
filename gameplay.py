#****************************************************
# Put all constants below
#****************************************************
NUMBER_OF_HOLES = 7

#****************************************************
# Fill each hole with a certain number of seed
#****************************************************
def fill_holes(holes, seed):
    for i in range(NUMBER_OF_HOLES):
        holes.append(seed)

#****************************************************
# Move seed clockwise and stop based on the rules
#****************************************************
def move_seeds(index, hl_player, hl_opponent, hs_player, house_opponent, seed):
    # take all seed
    holes_player = []
    for hole in hl_player:
        holes_player.append(hole)
        
    holes_opponent = []
    for hole in hl_opponent:
        holes_opponent.append(hole)
        
    house_player = []
    for hole in hs_player:
        house_player.append(hole)
    seed = holes_player[index]
    
    if (seed != 0):
        holes_player[index] = 0
    
        # initialization
        play_condition = True
        start_idx = index+1
        last_idx = start_idx
        last_position = 'holes_player'
        
        # loop till stop condition
        while play_condition:
            # move seed around player's holes
            for i in range(start_idx, NUMBER_OF_HOLES):
                holes_player[i] += 1
                seed -= 1
    
                last_idx = i
                last_position = 'holes_player'
    
                # when number of seed in hand is 0
                if (seed == 0 and holes_player[last_idx] == 1):
                    play_condition = False
                elif (seed == 0 and holes_player[last_idx] > 1):
                    seed = holes_player[last_idx]
                    holes_player[last_idx] = 0
    
                if not(play_condition):
                    break
            
            if not(play_condition):
                break
    
            start_idx = 0
    
            # put seed into player's house
            house_player[0] += 1
            seed -= 1
    
            last_position = 'house'
    
            # when number of seed in hand is 0
            if (seed == 0 and last_position == 'house'):
                play_condition = False
            
            if not(play_condition):
                break
    
            # move seed around opponent's holes
            for i in range(NUMBER_OF_HOLES):
                holes_opponent[i] += 1
                seed -= 1
    
                last_idx = i
                last_position = 'holes_opponent'
    
                # when number of seed in hand is 0
                if (seed == 0 and holes_opponent[last_idx] == 1):
                    play_condition = False
                elif (seed == 0 and holes_opponent[last_idx] > 1):
                    seed = holes_opponent[last_idx]
                    holes_opponent[last_idx] = 0
    
                if not(play_condition):
                    break
            
            if not(play_condition):
                break
    
        # stop in player's hole and across opponent's hole is not empty
        if last_position == 'holes_player' and holes_opponent[NUMBER_OF_HOLES-last_idx-1] != 0:
            house_player[0] += (holes_player[last_idx] + holes_opponent[NUMBER_OF_HOLES-last_idx-1])
            holes_player[last_idx] = 0
            holes_opponent[NUMBER_OF_HOLES-last_idx-1] = 0
    
    return (holes_player, holes_opponent, house_player, house_opponent)