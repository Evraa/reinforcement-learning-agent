import random

def random_agent_start(board,N,M):
    x = int(random.randint(0,N-1))
    y = int(random.randint(0,M-1))

    while board.board[x][y] != 0:
        x = int(random.randint(0,N-1))
        y = int(random.randint(0,M-1))
    return x,y


def find_neighbours(board, x, y):
    top = [x-1, y]
    bottom = [x+1, y]
    left = [x, y-1]
    right = [x, y+1]
    valid_moves = []

    if not board.check_invalid_index(top):
        valid_moves.append(top)
    if not board.check_invalid_index(bottom):
        valid_moves.append(bottom)
    if not board.check_invalid_index(left):
        valid_moves.append(left)
    if not board.check_invalid_index(right):
        valid_moves.append(right)
    
    return valid_moves
        
def move(policy_board, valid_moves,x, y, eps):
    # random epsilon (eps-greedy)
    rand = random.random() #[0,1)
    if rand > eps: #80% chance
        #what is policy?
        if policy_board[x][y] == "r" and [x, y+1] in valid_moves:
            return [x, y+1]
        if policy_board[x][y] == "l" and [x, y-1] in valid_moves:
            return [x, y-1]
        if policy_board[x][y] == "t" and [x-1, y] in valid_moves:
            return [x-1, y]
        if policy_board[x][y] == "b" and [x+1, y] in valid_moves:
            return [x+1, y]
        
        # policy is invalid
        # go random
        return random.choice(valid_moves)
    else:
        # go random 20%
        return random.choice(valid_moves)

def reward_to_go(board,policy_board, epochs, eps=0):
    '''
    '''
    # get board dimenstions
    N, M = board.get_dim()
    # tabular
    results = []
        
    for ep in range (epochs):
        # assign position for agent
        x,y = random_agent_start(board,N,M)
        # store one path record
        result = []
        while True:
            # find out valid moves
            valid_moves = find_neighbours(board, x, y)
            # pick move
            x_new, y_new = move(policy_board, valid_moves,x, y, eps)
            # store results
            result.append([x,y])
            # check termination
            if board.board[x_new][y_new] == 1 or board.board[x_new][y_new] == -1:
                # terminate
                result.append([x_new,y_new])
                results.append(result)
                break
            # another one
            x,y = x_new, y_new
    return results

def interpret_results(results, sb):
    # get board dimenstions
    N, M = sb.get_dim()
    utilities = []
    for i in range(N):
        utility_row = []
        for j in range(M):
            if sb.board[i][j] == 0:
                # calculate all of its occurences at the table
                utility = []
                for result in results:
                    if [i,j] in result:
                        value = 0
                        for index in reversed(result):
                            value += sb.get_state_value(index[0],index[1])
                            if index == [i,j]: break
                        utility.append(value)

                if len(utility) == 0:
                    utility_row.append(0)                    
                else:
                    utility_row.append(sum(utility)/len(utility))
            else:
                utility_row.append(0)
        utilities.append(utility_row)
    return utilities