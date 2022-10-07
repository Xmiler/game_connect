from connect_4 import Board, CONNECT_NUMBER


def test_board__check_directoin_horizontal():
    board = Board()
    board._state[-1, :CONNECT_NUMBER] = 0
    assert board._check_direction(0, (0, board.rows-1), 1, 0)


def test_board__check_directoin_vertical():
    board = Board()
    board._state[-CONNECT_NUMBER:, 0] = 0
    assert board._check_direction(0, (0, board.rows-1), 0, 1)


def test_board__check_directoin_diagonal_upper_right():
    board = Board()
    for i in range(CONNECT_NUMBER):
        board._state[board.rows-1-i, i] = 0
    assert board._check_direction(0, (0, board.rows-1), 1, -1)


def test_board__check_directoin_diagonal_upper_left():
    board = Board()
    for i in range(CONNECT_NUMBER):
        board._state[board.rows-1-i, board.columns-1-i] = 0
    assert board._check_direction(0, (board.columns-1, board.rows-1), 1, 1)
