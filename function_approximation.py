import numpy as np
import math
import random



def get_avg(listy):
    listy_np = np.array(listy)
    return listy_np.mean(axis=0)

def euc_distance(a,b,x,y):
    return math.sqrt(pow((a-x),2) + pow((b-y),2))

def compute_features(sb, add_euc=False):
    board = sb.board
    goal = get_avg(sb.get_goals())

    N,M = sb.get_dim()
    features = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                # calc its features
                if add_euc:
                    feature = [1,i,j,euc_distance(i,j,goal[0],goal[1])]
                    features.append(feature)
                else:
                    features.append([1,i,j])
    return features

def init_weights(dim):
    ws = []
    for i in range (dim):
        ws.append(random.random())
    return ws

