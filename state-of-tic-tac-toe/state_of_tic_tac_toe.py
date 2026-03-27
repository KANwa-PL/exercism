
def gamestate(board):
    columns = list(zip(*board))
    columns = ["".join(col) for col in columns]
    diagonals = [board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]]
    combined = board + columns + diagonals

    win_x = False
    win_y = False
    count_x = 0
    count_y = 0
    count_empty = 0

    for element in combined:
        if element == "XXX":
            win_x = True
        elif element == "OOO":
            win_y = True

    for element in board:
        for character in element:
            if character == "X":
                count_x += 1
            elif character == "O":
                count_y += 1
            else:
                count_empty += 1

    if win_x and win_y:
        raise ValueError("Impossible board: game should have ended after the game was won")
    elif count_x < count_y:
        raise ValueError("Wrong turn order: O started")
    elif count_x - count_y > 1:
        raise ValueError("Wrong turn order: X went twice")
    elif win_x:
        return "win"
    elif win_y:
        return "win"
    elif count_empty > 0:
        return "ongoing"
    return "draw"

