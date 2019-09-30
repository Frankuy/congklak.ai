#****************************************************
# Import all function needed
#****************************************************
from gameplay import *
import random

#****************************************************
# Put all global variables below
#****************************************************
holes_player = []
holes_opponent = []
house_player = [0]
house_opponent = [0]
seed = 0

#****************************************************
# Construct the game set
#****************************************************
fill_holes(holes_player, 7)
fill_holes(holes_opponent, 7)

#****************************************************
# Play the game
#****************************************************
index = random.randint(0, NUMBER_OF_HOLES-1)
print(index)
print(move_seeds(index, holes_player, holes_opponent, house_player, house_opponent, seed))