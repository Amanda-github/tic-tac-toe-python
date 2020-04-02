import random
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
current_player = "X"
count = 0
winner = False


def print_board():
    for rows in reversed(board):
        print(rows)


print_board()


def valid_check(x, y):
    if -1 < x < 3 and -1 < y < 3:
        if board[y][x] == "_":
            return True
        else:
            print("space taken")
    else:
        print("input between 0 and 2")


def winner_player():

    win_combos = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combo in win_combos:
        win_condition = []
        for i in combo:
            win_condition.append(board[i[0]][i[1]])
        win_condition = "".join(win_condition)
        if win_condition == "XXX":
            print("X")
            return True
        elif win_condition == "OOO":
            print("O")
            return True
        elif count == 9:
            print("draw")
            return True


def computer_smart():
    win_combos = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    new_coords = []
    for combo in win_combos:
        win_condition = []
        for i in combo:
            win_condition.append(board[i[0]][i[1]])
        win_condition = "".join(win_condition)
        if win_condition.count('_') == 1:
            if win_condition.count("X") == 2:
                new_coords = combo[win_condition.index('_')]
                print(new_coords)
            elif win_condition.count("O") == 2:
                return(combo[win_condition.index('_')])

            # elif new_coords == []:
            #     new_coords = [random.randint(0, 2), random.randint(0, 2)]
        elif ((win_condition.count('_') > 1) and new_coords == []):
            new_coords = [random.randint(0, 2), random.randint(0, 2)]
    # if new_coords == []:
    #     new_coords = [random.randint(0, 2), random.randint(0, 2)]

    return new_coords


def change_player(player):
    global current_player
    if player == "X":
        current_player = "O"
    else:
        current_player = "X"


def gameplay(X, Y):
    global count
    if valid_check(X, Y):

        board[Y][X] = current_player
        print_board()
        count += 1

        if winner_player():
            return True

        change_player(current_player)


while not winner:
    print(f"Current Player is {current_player}")
    if current_player == 'X':
        X = int(input("Input X coordinate"))
        Y = int(input("Input Y coordinate"))

        if gameplay(X, Y):
            winner = True
            break
    else:
        com_coords = computer_smart()
        X = com_coords[1]
        Y = com_coords[0]
        if gameplay(X, Y):
            winner = True
            break
