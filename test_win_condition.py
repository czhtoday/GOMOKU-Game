import pytest
from win_condition import Win

def test_check_line():
    # Test with an empty board
    empty_board = [[0 for _ in range(15)] for _ in range(15)]
    assert not Win.check_line(empty_board, 15, 15)

    # Test with a board having a winning condition
    winning_board = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(5):
        winning_board[0][i] = 1  # Simulating a row of five stones
    assert Win.check_line(winning_board, 15, 15)

    # Test with a non-winning board
    non_winning_board = [[0 for _ in range(15)] for _ in range(15)]
    non_winning_board[0][0] = 1
    non_winning_board[1][1] = 1
    non_winning_board[2][2] = 1
    assert not Win.check_line(non_winning_board, 15, 15)

