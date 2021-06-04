import numpy as np
import sys
import random

def get_avg(listy):
    listy_np = np.array(listy)
    return listy_np.mean(axis=0)



def direction(i,j,x,y):
    tot = abs(x-i) + abs(y-j)
    rand = random.random() #[0,1)
    if tot == 0:
        # same point
        return 'same'
    if abs(x-i) > abs(y-j):
        if abs(y-j)/tot >= rand:
            # surprisingly favourite y
            if y>j: return "r"
            else: return "l"
        else:
            # favourite x
            if x>i: return "b"
            else: return "t"
    else:
        if abs(x-i)/tot >= rand:
            # surprisingly favourite x
            if x>i: return "b"
            else: return "t"
        else:
            # favourite y
            if y>j: return "r"
            else: return "l"


def invert_policy(symbol):
    if symbol == "r":return "l"
    if symbol == "l":return "r"
    if symbol == "t":return "b"
    if symbol == "b":return "t"
    if symbol == "same":return "same"
    
    

def get_policy(board, policy="goal"):
    # find all goals i,j
    N,M = board.get_dim()
    # get goals
    if policy=="goal":
        goals = board.get_goals()
    elif policy=="exit":
        goals = board.get_exits()

    if len(goals) == 0: 
        print ("Error: can't find any goal/exit")
        sys.exit(1)
    
    avg_point = get_avg(goals)
    policy_board = []
    for i in range (N):
        policy_row = []
        for j in range (M):
            d = direction(i,j,avg_point[0],avg_point[1])
            if policy =="exit": 
                d = invert_policy(d)
            print (i,j)
            print (d)
            policy_row.append(d)
        policy_board.append(policy_row)

    return policy_board

def get_const_policy():
    return [
        ["r","r","r","same"],
        ["t","same","t","same"],
        ["t","l","l","l"]
    ]