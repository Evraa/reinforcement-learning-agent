

class StateBoard:
    """
    Stating board info
    """
    def __init__(self, N, M, agent_i=0, agent_j=0, void_cost=-0.04, goal_cost=5, exit_cost=-5, state=0):
        self.N = N
        self.M = M
        self.state_value = {}
        self.state_value[0] = void_cost
        self.state_value[1] = goal_cost
        self.state_value[-1] = exit_cost
        self.state_value[2] = 0
        self.agent = [agent_i, agent_j]
        self.policy = []
        self.board = []
        for _ in range (N):
            row = []
            for _ in range (M): row.append(state)
            self.board.append(row)

        

    def assign_goal(self, i, j, state=1):
        assert i<self.N and j<self.M, "Out of bound assignment!"
        try:
            self.board[i][j] = state
        except:
            print ("Error: cant assign goal state")
    
    def assign_exit(self, i, j, state=-1):
        assert i<self.N and j<self.M, "Out of bound assignment!"
        try:
            self.board[i][j] = state
        except:
            print ("Error: cant assign exit state")

    def assign_obstacle(self, i, j, state=2):
        assert i<self.N and j<self.M, "Out of bound assignment!"
        try:
            self.board[i][j] = state
        except:
            print ("Error: cant assign obstacle state")
        
    
    def print_board(self):
        print (self.board)
        print ("State vlaues:")
        temp_state = []
        for i in range(self.N):
            temp_row = []
            for j in range (self.M): temp_row.append(self.state_value[self.board[i][j]])
            temp_state.append(temp_row)
        print (temp_state)


    def get_dim(self):
        return self.N, self.M

    def check_invalid_index(self, coord):
        if coord[0] <0 or coord[1]<0 or coord[0] >= self.N or coord[1]>=self.M:
            return True
        if self.board[coord[0]][coord[1]] == 2:
            return True
        return False

    def get_goals(self):
        goals = []
        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == 1:
                    goal = [i,j]
                    goals.append(goal)
        return goals

    def get_exits(self):
        exits = []
        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == -1:
                    exit = [i,j]
                    exits.append(exit)
        return exits

    def assing_policy(self, policy_board):
        self.policy = policy_board
