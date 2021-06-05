import board, graph, policy, direct_utility_estimation, function_approximation



def get_act(N,M, uts):
    act_val = []
    for i in range (N):
        for j in range(M):
            if uts[i][j] != 0:
                act_val.append(uts[i][j])
    return act_val


if __name__ == "__main__":
    # print ("Welcome to CMP402B")
    # print ("This program works in several modes and options, showing GUI for demonstration")
    # print ("First: you need to pick board size: ")
    # rows = int(input ("No. of Rows: "))
    # cols = int(input ("No. of Columns: "))
    # sb = board.StateBoard(rows, cols)
    # print ("Great, Now..")
    # exit = False
    # while not exit:
    #     print ("To assign a GOAL press g")
    #     print ("To assign a Exit press e")
    #     print ("To assign a Obstacle press o")
    #     print ("To go to next step press n")
    #     print ("To redefine the board press b")
    #     print ("To exit press ctrl+z")
    #     opt = str(input ("Option: "))

    #     if opt == "g":
    #         x = int(input ("X = "))
    #         y = int(input ("Y = "))
    #         v = int(input("Value = "))
    #         sb.assign_goal(x,y,state=v)

    #     elif opt == "e":
    #         x = int(input ("X = "))
    #         y = int(input ("Y = "))
    #         v = int(input("Value = "))
    #         sb.assign_exit(x,y,state=v)

    #     elif opt == "o":
    #         x = int(input ("X = "))
    #         y = int(input ("Y = "))
    #         v = int(input("Value = "))
    #         sb.assign_obstacle(x,y,state=v)
            
    #     elif opt == "n":
    #         exit = True
    #     elif opt == "b":
            
    #     else:
    #         print ("Error: invalid input!")
    
    sb = board.StateBoard(10,10)
    
    sb.assign_goal(4,4)
    sb.assign_exit(4,5)
    # sb.assign_exit(9,8)
    # sb.assign_exit(5,9)
    # sb.assign_obstacle(1,1)

    N,M = sb.get_dim()
    policy_board = policy.get_policy(sb, policy="goal")
    # policy_board = policy.get_const_policy()
    sb.assing_policy(policy_board)

    db = graph.DrawBoard(N,M)
    db.draw_board(sb)

    results = direct_utility_estimation.reward_to_go(sb, policy_board, 1000,eps=0.2)
    uts = direct_utility_estimation.interpret_results(results, sb)
    actual_values = get_act(N,M, uts)
    db.draw_board_text(sb, uts)

    uts = function_approximation.run(epochs=1000, sb=sb, results=results, add_euc=False)
    db.draw_board_text(sb, uts, fa=True)
    # uts = function_approximation.run(epochs=1000, sb=sb, add_euc=False)
    # db.draw_board_text(sb, uts, fa=True)
