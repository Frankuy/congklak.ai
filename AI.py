from gameplay import *
MAX_DEPTH = 3
state = holes_player, holes_opponent, house_player, house_opponent
arr=[]
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
x = holes_player, holes_opponent, house_player, house_opponent
arr=[]
def evaluation(state):
	return (sum(state[2])-sum(state[3]))*1000+(sum(state[1])-sum(state[0]))
def make_tree(state,depth):
    global arr
    if (depth==MAX_DEPTH):
        arr.append(evaluation(state))
    else:
        for i in range(7):
            if (depth%2):
                make_tree(move_seeds(i,state[0],state[1],state[2],state[3],0),depth+1)
            else:
                make_tree(move_seeds(i,state[1],state[0],state[3],state[2],0),depth+1)  
make_tree(x,0)
print(arr)
