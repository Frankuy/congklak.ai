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
print("LET'S PLAY CONGKLAK")
print("Choose your mode !")
print("1. Player vs Player")
print("2. Player vs Random Bot (Without AI)")
mode = int(input(">> "))
while (mode < 1) or (mode > 2):
    print("Wrong input !")
    mode = int(input(">> "))

#****************************************************
# Player vs player mode
#****************************************************
if mode == 1:
    turn = 1
    while (sum(holes_player) + sum(holes_opponent)) != 0:
        result = []
        input_valid = False
        if turn == 1:
            print("PLAYER 1 TURN")
            print("Holes player 1 : " + str(holes_player))
            print("Holes player 2 : " + str(holes_opponent))
            print("House player 1 : " + str(house_player))
            print("House player 2 : " + str(house_opponent))
            index = int(input("Choose the hole >> "))
            while not(input_valid):
                if (index < 0) or (index > 6):
                    print("Wrong input !")
                    index = int(input("Choose the hole >> "))
                else:
                    if holes_player[index] == 0:
                        print("No seed in that hole !")
                        index = int(input("Choose the hole >> "))
                    else:
                        input_valid = True
            result = move_seeds(index, holes_player, holes_opponent, house_player, house_opponent, seed)
            holes_player = []
            holes_player.extend(result[0])
            holes_opponent = []
            holes_opponent.extend(result[1])
            house_player = []
            house_player.extend(result[2])
            house_opponent = []
            house_opponent.extend(result[3])
            turn = 2
        else:
            print("PLAYER 2 TURN")
            print("Holes player 1 : " + str(holes_player))
            print("Holes player 2 : " + str(holes_opponent))
            print("House player 1 : " + str(house_player))
            print("House player 2 : " + str(house_opponent))
            index = int(input("Choose the hole >> "))
            while not(input_valid):
                if (index < 0) or (index > 6):
                    print("Wrong input !")
                    index = int(input("Choose the hole >> "))
                else:
                    if holes_opponent[index] == 0:
                        print("No seed in that hole !")
                        index = int(input("Choose the hole >> "))
                    else:
                        input_valid = True
            result = move_seeds(index, holes_opponent, holes_player, house_opponent, house_player, seed)
            holes_opponent = []
            holes_opponent.extend(result[0])
            holes_player = []
            holes_player.extend(result[1])
            house_opponent = []
            house_opponent.extend(result[2])
            house_player = []
            house_player.extend(result[3])
            turn = 1
    print("RESULT !!!")
    print("Holes player 1 : " + str(holes_player))
    print("Holes player 2 : " + str(holes_opponent))
    print("House player 1 : " + str(house_player))
    print("House player 2 : " + str(house_opponent))
    if (sum(house_player) > sum(house_opponent)):
        print("PLAYER 1 WIN")
    else:
        print("PLAYER 2 WIN")

#****************************************************
# Player vs random bot mode
#****************************************************
elif mode == 2:
    turn = 1
    while (sum(holes_player) + sum(holes_opponent)) != 0:
        result = []
        input_valid = False
        if turn == 1:
            print("PLAYER TURN")
            print("Holes player 1 : " + str(holes_player))
            print("Holes player 2 : " + str(holes_opponent))
            print("House player 1 : " + str(house_player))
            print("House player 2 : " + str(house_opponent))
            index = int(input("Choose the hole >> "))
            while not(input_valid):
                if (index < 0) or (index > 6):
                    print("Wrong input !")
                    index = int(input("Choose the hole >> "))
                else:
                    if holes_player[index] == 0:
                        print("No seed in that hole !")
                        index = int(input("Choose the hole >> "))
                    else:
                        input_valid = True
            result = move_seeds(index, holes_player, holes_opponent, house_player, house_opponent, seed)
            holes_player = []
            holes_player.extend(result[0])
            holes_opponent = []
            holes_opponent.extend(result[1])
            house_player = []
            house_player.extend(result[2])
            house_opponent = []
            house_opponent.extend(result[3])
            turn = 2
        else:
            print("BOT TURN")
            print("Holes player 1 : " + str(holes_player))
            print("Holes player 2 : " + str(holes_opponent))
            print("House player 1 : " + str(house_player))
            print("House player 2 : " + str(house_opponent))
            index = random.randint(0, NUMBER_OF_HOLES-1)
            print("Choose the hole >> " + str(index))
            while not(input_valid):
                if holes_opponent[index] == 0:
                    print("No seed in that hole !")
                    index = random.randint(0, NUMBER_OF_HOLES-1)
                    print("Choose the hole >> " + str(index))
                else:
                    input_valid = True
            result = move_seeds(index, holes_opponent, holes_player, house_opponent, house_player, seed)
            holes_opponent = []
            holes_opponent.extend(result[0])
            holes_player = []
            holes_player.extend(result[1])
            house_opponent = []
            house_opponent.extend(result[2])
            house_player = []
            house_player.extend(result[3])
            turn = 1
    print("RESULT !!!")
    print("Holes player 1 : " + str(holes_player))
    print("Holes player 2 : " + str(holes_opponent))
    print("House player 1 : " + str(house_player))
    print("House player 2 : " + str(house_opponent))
    if (sum(house_player) > sum(house_opponent)):
        print("PLAYER WIN")
    else:
        print("BOT WIN")