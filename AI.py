from gameplay import *
MAX_DEPTH = 3
#state = holes_player, holes_opponent, house_player, house_opponent
holes_player = []
holes_opponent = []
house_player = [0]
house_opponent = [0]
seed = 0

fill_holes(holes_player, 7)
fill_holes(holes_opponent, 7)

x = holes_player, holes_opponent, house_player, house_opponent
arr=[]
def evaluation(state):
	return (sum(state[2])-sum(state[3]))*1000+(sum(state[1])-sum(state[0]))

counter = 0
def make_tree(state,depth,step,alpha,beta):
    global counter
    if (depth==MAX_DEPTH):
        return [evaluation(state),step]
    else:
        if (depth%2): #Seek minimum value
            minmax_point = 100000
            for i in range(7):
                temp_point = make_tree(move_seeds(i,state[1],state[0],state[3],state[2],0),depth+1,step,alpha,beta)
                minmax_point = min(minmax_point,temp_point[0])
                beta = min(minmax_point,beta)
                if (alpha>=beta):
                    break
            
            return [beta, step]
            
        else: #Seek maximum value
            minmax_point = -100000
            for i in range(7): 
                if (depth==0): 
                    temp_point = make_tree(move_seeds(i,state[0],state[1],state[2],state[3],0),depth+1,i,alpha,beta)
                else:
                    temp_point = make_tree(move_seeds(i,state[0],state[1],state[2],state[3],0),depth+1,step,alpha,beta)
                minmax_point = max(minmax_point,temp_point[0])
                alpha = max(minmax_point,alpha)
                if (alpha>=beta):
                    break
                    
            return [alpha, step]
                           
        
print(make_tree(x, 0, 0, -100000, 100000))
