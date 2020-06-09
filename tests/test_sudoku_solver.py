import pytest

from source import sudoku_solver


@pytest.mark.parametrize('board, expected_result', [
    (
        [
            [0, 0, 0, 6, 0, 0, 4, 0, 0],
            [7, 0, 0, 0, 0, 3, 6, 0, 0],
            [0, 0, 0, 0, 9, 1, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 1, 8, 0, 0, 0, 3],
            [0, 0, 0, 3, 0, 6, 0, 4, 5],
            [0, 4, 0, 2, 0, 0, 0, 6, 0],
            [9, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 1, 0, 0],
        ],
        [
            [5, 8, 1, 6, 7, 2, 4, 3, 9],
            [7, 9, 2, 8, 4, 3, 6, 5, 1],
            [3, 6, 4, 5, 9, 1, 7, 8, 2],
            [4, 3, 8, 9, 5, 7, 2, 1, 6],
            [2, 5, 6, 1, 8, 4, 9, 7, 3],
            [1, 7, 9, 3, 2, 6, 8, 4, 5],
            [8, 4, 5, 2, 1, 9, 3, 6, 7],
            [9, 1, 3, 7, 6, 8, 5, 2, 4],
            [6, 2, 7, 4, 3, 5, 1, 9, 8],
        ]
    ),
    (
        [
            [1, 0, 0, 4, 8, 9, 0, 0, 6],
            [7, 3, 0, 0, 5, 0, 0, 4, 0],
            [4, 6, 0, 0, 0, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 0, 6, 0, 0],
            [5, 0, 1, 7, 0, 3, 0, 0, 8],
            [0, 4, 6, 0, 9, 5, 7, 1, 0],
            [9, 1, 4, 6, 0, 0, 0, 8, 0],
            [0, 2, 0, 0, 4, 0, 0, 3, 7],
            [8, 0, 3, 5, 1, 2, 0, 0, 4],
        ],
        [
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4],
        ]
    )
])
def test_solver(mocker, board, expected_result):
    mocker.patch.object(sudoku_solver, 'time')
    board = board
    solved_board, _ = sudoku_solver.solver(board)
    assert solved_board == expected_result


@pytest.mark.parametrize('board, expected_result', [
    (
        [[0]],
        (0, 0)
    ),
    (
        [[1], [0]],
        (1, 0)
    ),
    (
        [[1, 0]],
        (0, 1)
    ),
    (
        [[1]],
        None
    ),
])
def test_find_empty(board, expected_result):
    assert sudoku_solver.find_empty(board) == expected_result


@pytest.mark.parametrize('row_index, column_index, n, expected_result', [
    (
        0,
        1,
        2,
        True
    ),
    (
        0,
        1,
        8,
        False
    ),
    (
        0,
        1,
        3,
        False
    ),
    (
        0,
        1,
        7,
        False
    )
])
def test_valid_move(row_index, column_index, n, expected_result):
    board = [
        [1, 0, 0, 4, 8, 9],
        [7, 3, 0, 0, 5, 0],
        [4, 6, 0, 0, 0, 1],
        [3, 8, 7, 1, 2, 0],
        [5, 0, 1, 7, 0, 3],
        [0, 4, 6, 0, 9, 5],
    ]
    assert sudoku_solver.valid_move(row_index, column_index, n, board) == expected_result
