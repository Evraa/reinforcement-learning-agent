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
    board = sb.board
    policy_board = sb.policy
    result = []
    while True:
        # find out valid moves
        valid_moves = direct_utility_estimation.find_neighbours(sb, x, y)
        # pick move
        x_new, y_new = direct_utility_estimation.move(policy_board, valid_moves,x, y, eps=0.5)
        # store results
        result.append([x,y])
        # check termination
        if sb.board[x_new][y_new] == 1 or sb.board[x_new][y_new] == -1:
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
    board = sb.board
    actual_values = []
    for i in range(N):
        for j in range(M):
            print (f'node: {i,j}')
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


def loss(actual, predicted):
    # no need to compute the loss
    return 0


def forward(features, ws):
    # estimate
    predictions = []
    for exm in features:
        pred = np.multiply(exm, ws)
        predictions.append(np.sum(pred))
    return predictions

def update_weights(sb, ws, lr, actual_values, predictions, features):
    N,M = sb.get_dim()
    board = sb.board
    k = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                for l,w in enumerate(ws):
                    w += lr * (actual_values[k] - predictions[k]) * features[k][l]
                k += 1
    return ws


def calc_uts(sb, ws):
    N,M = sb.get_dim()
    board = sb.board
    uts = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                val = np.multiply([1,i,j], ws)
                uts.append(np.sum(val))
    return uts

def run(epochs, sb):
    features = compute_features(sb)
    ws = init_weights(3)
    actual_values = run_trials(sb)
    lr = 0.1
    for epoch in range(epochs):
        print (f'Epoch: {epoch}')
        predictions = forward(features, ws)
        ws = update_weights(sb, ws, lr, actual_values, predictions, features)

    return calc_uts(sb, ws)

