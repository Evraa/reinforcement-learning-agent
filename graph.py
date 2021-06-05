from graphics import *

class DrawBoard:
    """
    Drawing the board given N
    """
    def __init__(self, N,M):
        self.N = M
        self.M = N
        self.norm_color = color_rgb(97, 157, 246)         #0
        self.goal_color = color_rgb(97, 246, 142)         #1
        self.exit_color = color_rgb(246, 97, 97)          #-1
        self.obstacle_color = color_rgb(110, 110, 110)    #2
        self.arrow_color = color_rgb(0,0,0)  
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
    
    def line(self, center_x, center_y, color, direction):
        if direction == "r" or direction == "l":
            point_1 = Point(center_x-5, center_y)
            point_2 = Point(center_x+5, center_y)
            line = Line(point_1, point_2)
            line.setFill(self.arrow_color)
            if direction == "r":
                line.setArrow("last")
            else:
                line.setArrow("first")
            line.draw(self.window)

        if direction == "t" or direction == "b" :
            point_1 = Point(center_x, center_y-5)
            point_2 = Point(center_x, center_y+5)
            line = Line(point_1, point_2)
            if direction == "t":
                line.setArrow("last")
            else:
                line.setArrow("first")
            line.setFill(self.arrow_color)
            line.draw(self.window)
    
    def text(self, center_x, center_y, color, ut):
        point = Point(center_x, center_y)
        text = Text(point, str(ut))
        text.setTextColor(color)
        text.draw(self.window)

    def draw_board(self, sb):
        self.set_window()
        # Draw squares
        # Rows
        for i in range (self.M): #3
            # Columns
            for j in range (self.N):    #4
                policy_flag = False
                if sb.board[self.M-i-1][j] == 0:
                    # normal blcok
                    color = self.norm_color
                    policy_flag = True
                elif sb.board[self.M-i-1][j] == 1:
                    # goal
                    color = self.goal_color
                elif sb.board[self.M-i-1][j] == -1:
                    # exit
                    color = self.exit_color
                elif sb.board[self.M-i-1][j] == 2:
                    # obstacle
                    color = self.obstacle_color
                
                self.rect(j*30, i*30, color)
                if policy_flag: # draw policy
                    self.line((j*30)+15, (i*30)+15, self.arrow_color, sb.get_policy_value(self.M-i-1,j))

        self.window.getMouse()
        # self.window.close()

    def draw_board_text(self, sb, uts, fa=False):
        self.set_window()
        # Draw squares
        # Rows
        k = 0
        for i in range (self.M): #3
            # Columns
            for j in range (self.N):    #4
                text_flag = False
                if sb.board[self.M-i-1][j] == 0:
                    # normal blcok
                    color = self.norm_color
                    text_flag = True
                elif sb.board[self.M-i-1][j] == 1:
                    # goal
                    color = self.goal_color
                elif sb.board[self.M-i-1][j] == -1:
                    # exit
                    color = self.exit_color
                elif sb.board[self.M-i-1][j] == 2:
                    # obstacle
                    color = self.obstacle_color
                
                self.rect(j*30, i*30, color)
                if text_flag: # draw policy
                    if fa:
                        ut = format( uts[k] , '.2f')
                        k += 1
                    else:
                        ut = format( uts[self.M-i-1][j] , '.2f')
                    self.text((j*30)+15, (i*30)+15, self.arrow_color, ut)

        self.window.getMouse()
        # self.window.close()
