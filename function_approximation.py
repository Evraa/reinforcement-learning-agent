import numpy as np
import math

def get_avg(listy):
    listy_np = np.array(listy)
    return listy_np.mean(axis=0)

def euc_distance(a,b,x,y):
    return math.sqrt(pow((a-x),2) + pow((b-y),2))


def init_weights(dim):
    ws = []
    for i in range (dim):
        ws.append(0)
    return ws


def calc_uts(sb, ws, add_euc=False):
    '''
        For each point on the grid, get its estimated value after training.
    '''
    N,M = sb.get_dim()
    board = sb.board
    goal = get_avg(sb.get_goals())
    uts = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                if add_euc:
                    val = np.multiply([1,i,j,euc_distance(i,j,goal[0],goal[1]) ], ws)
                else:
                    val = np.multiply([1,i,j], ws)
                uts.append(np.sum(val))
    return uts


def predict(index, add_euc, ws, goal):
    '''
        Whether using ueclidean distance from the goal as an estimation in our func appr.

        Calculate the predicted value of this cell with the so far calculated weights.
    '''
    i,j = index
    if add_euc:
        val = np.sum(np.multiply([1,i,j,euc_distance(i,j,goal[0],goal[1]) ], ws))
    else:
        val = np.sum(np.multiply([1,i,j], ws))
    return val

def fa(results, ws, sb, lr, add_euc, goal):
    '''
        + Function approximation.
        + for each trial in our tabular form, we find the error between the actual value
            and the predicted ones
        + then update the weights (thetas)
    '''
    for result in results:
        act = 0
        skip_first = False
        for index in reversed(result):
            if not skip_first: 
                act += sb.get_state_value(index[0],index[1])
                skip_first = True
                continue

            # calculate prediction
            pred = predict(index, add_euc, ws, goal)
            # calculate difference
            act += sb.get_state_value(index[0],index[1])
            diff = act - pred
            # update thetas
            for l,w in enumerate(ws):
                if l == 0:
                    ws[l] += lr*diff
                elif l == 1:
                    ws[l] += lr*diff*index[0]
                elif l == 2:
                    ws[l] += lr*diff*index[1]
                elif l==3 and add_euc:
                    ws[l] += lr*diff*euc_distance(index[0],index[1],goal[0],goal[1])
    return ws

def run(epochs, sb, results, add_euc=False, lr=0.001):
    '''
        Main running loop.
        runs for number of epochs, on a given learning rate
        with the option of adding the euclidean distance to the goal as a feature.
    '''
    goal = get_avg(sb.get_goals())

    if add_euc:
        ws = init_weights(4)
    else:
        ws = init_weights(3)

    for epoch in range(epochs):
        print (f'Epoch: {epoch}')
        print (ws)
        ws_new = fa(results, ws, sb, lr, add_euc, goal)
        if ws == ws_new and epoch>20:
            print ("CONVERGENCE")
            break
        else:
            ws = ws_new
    return calc_uts(sb, ws, add_euc)

