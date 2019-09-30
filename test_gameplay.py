#****************************************************
# Import all function from gameplay.py
#****************************************************
from gameplay import *

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
index = 4
print(move_seeds(index, holes_player, holes_opponent, house_player, house_opponent, seed))