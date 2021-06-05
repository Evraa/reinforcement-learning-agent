import numpy as np
import math
import random
import direct_utility_estimation


def get_avg(listy):
    listy_np = np.array(listy)
    return listy_np.mean(axis=0)

def euc_distance(a,b,x,y):
    return math.sqrt(pow((a-x),2) + pow((b-y),2))

def run_trial(sb, x, y):
    board = sb.board()
    policy_board = sb.policy
    result = []
    while True:
        # find out valid moves
        valid_moves = direct_utility_estimation.find_neighbours(board, x, y)
        # pick move
        x_new, y_new = direct_utility_estimation.move(policy_board, valid_moves,x, y, eps=0)
        # store results
        result.append([x,y])
        # check termination
        if board.board[x_new][y_new] == 1 or board.board[x_new][y_new] == -1:
            # terminate
            result.append([x_new,y_new])
            break
        # another one
        x,y = x_new, y_new
    value = 0
    for index in reversed(result):
        value += sb.get_state_value(index[0],index[1])
        if index == [x,y]: 
            break
    return value


def run_trials(sb):
    N,M = sb.get_dim()
    board = sb.board()
    actual_values = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                actual_values.append(run_trial(sb, i, j))
    return actual_values



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



def forward(features, ws):
    pass