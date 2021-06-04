from graphics import *

class DrawBoard:
    """
    Drawing the board given N
    """
    def __init__(self, N,M):
        self.N = N
        self.M = M
        self.norm_color = color_rgb(97, 157, 246)         #0
        self.goal_color = color_rgb(97, 246, 142)         #1
        self.exit_color = color_rgb(246, 97, 97)          #-1
        self.obstacle_color = color_rgb(110, 110, 110)    #2
        self.agent_color = color_rgb(240,163, 47)         
    

    def set_window(self):
        win = GraphWin('board',720,720)
        win.setCoords(0, 0, self.N*30, self.M*30)
        self.window = win

    def rect(self, right, top, color):
        point_1 = Point(right, top)
        point_2 = Point(right+30, top+30)
        rect_draw = Rectangle(point_1, point_2)
        rect_draw.setFill(color)
        rect_draw.setOutline("black")
        rect_draw.draw(self.window)

    def circle(self, center_x, center_y, circle_color, radius=(30//2)-2):
        center = Point(center_x, center_y)
        circle_draw = Circle(center, radius)
        circle_draw.setFill(circle_color)
        circle_draw.setOutline("yellow")
        circle_draw.draw(self.window)
    

    def draw_board(self, board):
        self.set_window()
        # Draw squares
        # Rows
        for i in range (self.M): #3
            # Columns
            for j in range (self.N):    #4
                if board[self.M-i-1][j] == 0:
                    # normal blcok
                    color = self.norm_color
                elif board[self.M-i-1][j] == 1:
                    # goal
                    color = self.goal_color
                elif board[self.M-i-1][j] == -1:
                    # exit
                    color = self.exit_color
                elif board[self.M-i-1][j] == 2:
                    # obstacle
                    color = self.obstacle_color
                
                self.rect(j*30, i*30, color)

        self.window.getMouse()
        self.window.close()



# rows, cols = len(board),len(board[0])

# b = Board(cols,rows)
# b.draw_board(board)