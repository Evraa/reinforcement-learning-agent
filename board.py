

class StateBoard:
    """
    Stating board info
    """
    def __init__(self, N,M,val=0):
        self.N = N
        self.M = M
        self.board = [[val]*M]*N


    def assign_goal(self, i, j, val=1):
        assert i<self.N and j<self.M, "Out of bound assignment!"
        try:
            self.board[i][j] = val
        except:
            print ("Error: cant assign goal state")
    
    def assign_exit(self, i, j, val=-1):
        assert i<self.N and j<self.M, "Out of bound assignment!"
        try:
            self.board[i][j] = val
        except:
            print ("Error: cant assign exit state")

    def assign_obstacle(self, i, j, val=2):
        assert i<self.N and j<self.M, "Out of bound assignment!"
        try:
            self.board[i][j] = val
        except:
            print ("Error: cant assign obstacle state")
        
    
    def print_board(self):
        print (self.board)