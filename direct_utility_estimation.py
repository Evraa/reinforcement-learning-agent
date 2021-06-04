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
        if policy_board[x][y] == "r" and [x+1, y] in valid_moves:
            return [x+1, y]
        if policy_board[x][y] == "l" and [x-1, y] in valid_moves:
            return [x-1, y]
        if policy_board[x][y] == "t" and [x, y-1] in valid_moves:
            return [x, y-1]
        if policy_board[x][y] == "b" and [x, y+1] in valid_moves:
            return [x, y+1]
        
        # policy is invalid
        # go random
        return random.choice(valid_moves)
    else:
        # go random 20%
        return random.choice(valid_moves)

def reward_to_go(board,policy_board, epochs, eps=0.2):
    '''
    '''
    # get board dimenstions
    N, M = board.get_dim()
    # tabular
    results = []
    # assign position for agent
    x,y = random_agent_start(board,N,M)
        
    for _ in range (epochs):
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
                input (result)
                results.append(result)
                break
            # another one
            x,y = x_new, y_new
