board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

winner = False
current_player = "X"
count = 0


def print_board():
    for rows in reversed(board):
        print(rows)


print_board()


def valid_check(x, y):
    if -1 < x < 3 and -1 < y < 3:
        print('hi')
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


while not winner:
    print(f"Current Player is {current_player}")
    X = int(input("Input X coordinate"))
    Y = int(input("Input Y coordinate"))

    if valid_check(X, Y):

        board[Y][X] = current_player
        print_board()
        count += 1

        if winner_player():
            winner = True
            break

        if current_player == "X":
            current_player = "O"

        else:
            current_player = "X"
