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
index = 6
move_seeds(index, holes_player, holes_opponent, house_player, seed)

#****************************************************
# Print the result
#****************************************************
print(holes_player)
print(house_player[0])
print(holes_opponent)
print(house_opponent[0])