import board, graph, policy, direct_utility_estimation, function_approximation
import sys


def get_act(N,M, uts):
    act_val = []
    for i in range (N):
        for j in range(M):
            if uts[i][j] != 0:
                act_val.append(uts[i][j])
    return act_val


if __name__ == "__main__":
    print ("Welcome to CMP402B")
    print ("This program works in several modes and options, showing GUI for demonstration")
    print ("First: you need to pick board size: ")
    rows = int(input ("No. of Rows: "))
    cols = int(input ("No. of Columns: "))
    goal_cost = float(input("Goal cost: "))
    exit_cost = float(input("Exit cost: "))
    void_cost = float(input("Void cost: "))
    sb = board.StateBoard(rows, cols)
    print ("Great, Now..")
    exit = False
    while not exit:
        print ("To assign a GOAL press g")
        print ("To assign a Exit press e")
        print ("To assign a Obstacle press o")
        print ("To go to next step press n")
        print ("To redefine the board press b")
        print ("To exit press ctrl+z")
        opt = str(input ("Option: "))

        if opt == "g":
            x = int(input ("X = "))
            y = int(input ("Y = "))
            sb.assign_goal(x,y)

        elif opt == "e":
            x = int(input ("X = "))
            y = int(input ("Y = "))
            sb.assign_exit(x,y)

        elif opt == "o":
            x = int(input ("X = "))
            y = int(input ("Y = "))
            sb.assign_obstacle(x,y)
            
        elif opt == "n":
            exit = True

        elif opt == "b":
            del sb
            rows = int(input ("No. of Rows: "))
            cols = int(input ("No. of Columns: "))
            sb = board.StateBoard(rows, cols)
        else:
            print ("Error: invalid input!")
            sys.exit(1)


    print ("\nBoard: ")
    sb.print_board()
    print ("\n\nPOLICY: Some options needed to be picked.")
    if rows == 3 and cols == 4:
        print ("For the 3x4 world, which policy would you rather pick:")
        print ("Reference \t\t>> 0")
        print ("Towards Goal \t\t>> 1")
        print ("Away from Exit \t\t>> 2")
        opt = int(input ("Option: "))

    else:
        print ("For this world, which policy would you rather pick:")
        print ("Towards Goal \t\t>> 1")
        print ("Away from Exit \t\t>> 2")
        opt = int(input ("Option: "))

    print ("\n\nFunctions: Some options needed to be picked.")
    print ("Pick whether or not you want euclidean distance towards the goal to be added among the features as theta_4")
    opt_1 = int(input("To add press 1, othw. press 0\n"))

    print ("\n\nHow many Epochs/Trials for tabular trials?")
    epochs = int(input("E: "))

    print ("\n\nFor func apprx: what is desired learning rate alpha?")
    print ("Suggested: 0.001")
    lr = float(input("lr: "))

    print ("we're all set.")
    input("Press enter to start..")

    if opt == 0:
        policy_board = policy.get_const_policy()
    elif opt == 1:
        policy_board = policy.get_policy(sb, policy="goal")
    elif opt == 2:
        policy_board = policy.get_policy(sb, policy="exit")

    else:
        print ("Error: invalid input!")
        sys.exit(1)

    sb.assing_policy(policy_board)

    db = graph.DrawBoard(rows, cols)
    db.draw_board(sb)

    results = direct_utility_estimation.reward_to_go(sb, policy_board, epochs, eps=0.2)
    uts = direct_utility_estimation.interpret_results(results, sb)
    actual_values = get_act(rows, cols, uts)
    db.draw_board_text(sb, uts)

    if opt_1 == 1: 
        add_euc = True
    else:
        add_euc = False
    uts = function_approximation.run(epochs=100, sb=sb, results=results, add_euc=add_euc, lr=lr)
    db.draw_board_text(sb, uts, fa=True)
