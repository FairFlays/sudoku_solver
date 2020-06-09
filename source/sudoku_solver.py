import time

from sudoku_boards.medium.board_0.board import board_to_be_solved


def solver(board):
    start = time.time()
    solve(board)
    end = time.time() - start
    return board, end


def find_empty(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                return row, column
    return None


def solve(board):
    find = find_empty(board)
    if find is None:
        return True
    else:
        row_index, column_index = find

    for i in range(1, 10):
        if valid_move(row_index, column_index, i, board):
            board[row_index][column_index] = i
            if solve(board):
                return True
    board[row_index][column_index] = 0


def valid_move(row_index, column_index, n, board):
    column = [board[i][column_index] for i in range(len(board[row_index]))]
    box_x = column_index // 3
    box_y = row_index // 3

    if n in board[row_index] or n in column:
        return False

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == n:
                return False

    return True


def print_board(board):
    for row in range(len(board)):
        for column in range(len(board)):
            print(board[row][column], end=' ')
            if column in (2, 5):
                print('|', end=' ')
        print()
        if row in (2, 5):
            print('---------------------')
    print('\n~~~~~~~~~~~~~~~~~~~~~\n')


print_board(board_to_be_solved)
solved_board, time_spent = solver(board_to_be_solved)
print_board(solved_board)
print(f'Time spent - {time_spent}')
