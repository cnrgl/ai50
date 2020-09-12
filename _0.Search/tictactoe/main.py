"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def ncr(lst, n):
    # if n== 0 is not necessary
    if n == 0:
        return [[]]
    l = []
    for r in range(0, len(lst)):
        for p in ncr(lst[r + 1:], n - 1):
            l.append(lst[r] + p)
    return l


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # i == X - i == O --> if i=1 X or i=-1 O otherwise empty
    count = sum(sum((i == X)-(i == O) for i in x) for x in board)
    if count == 1:
        return X
    elif count == -1:
        return O
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                act.add((i, j))
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    act = actions(board) # possible actions
    move = board         # board template
    if action not in act:
        raise Exception("Action is not valid")
        return None
    if player(board) == X:
        move[action(0)][action[1]] = X
    elif player(board) == O:
        move[action[0]][action[1]] = O
    # final state
    else:
        return None
    return move


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    _x = set()
    _o = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                _x.add((i, j))
            elif board[i][j] == O:
                _o.add((i, j))
    for i in range(math.comb(len(_o), 3)):
        temp = _o[i-3:i]
        if sum(r[0] for r in temp) % 3 == 0 and sum(r[1] for r in temp) % 3 == 0:
            return O
    temp = ncr(_x, 3)
    for i in range(0, len(temp)):
        if sum(r[0] for r in temp) % 3 == 0 and sum(r[1] for r in temp) % 3 == 0:
            return X
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not winner(board):
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    return None


def max_value(board):
    if terminal(board):
        return utility(board)
        v = -1
        for act in actions(board):
            if result(board, act):
                v = max(v, min_value(result(board, act)))
        return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 1
    for act in actions(board):
        if result(board, act):
            v = min(v, max_value(result(board, act)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    mov=actions(board)[0]
    if terminal(board):
        return None
    if player(board) == X:
        v=-1
        for act in actions(board):
            if result(board, act):
                if max_value(board) > v:
                    mov = act
    if player(board) == O:
        v = 1
        for act in actions(board):
            if result(board, act):
                if min_value(board) < v:
                    mov = act
    return mov


def main():
    board=initial_state()


if __name__ == "main":
    main()
