import sys
import os
import string
import numpy as np
from tabulate import tabulate

CONNECT_NUMBER = 4
AVAILABLE_PLAYER_NAMES = list(string.ascii_uppercase)


class Board:
    def __init__(self, players_count=2, rows=6, columns=7):
        assert 2 <= players_count <= len(AVAILABLE_PLAYER_NAMES)
        assert 4 <= rows <= 100
        assert 4 <= columns <= 100

        self._players_count = players_count
        self._rows = rows
        self._columns = columns
        self._state = -1 * np.ones((rows, columns), dtype=np.int)
        self._player_names = AVAILABLE_PLAYER_NAMES[:players_count]

    def draw(self, player_id, mode):
        if mode == 'step':
            message = f'Step for the player "{self._player_names[player_id]}" ..'
        elif mode == 'win':
            message = f'The winner is "{self._player_names[player_id]}"'
        else:
            assert False
        os.system('clear')
        print(message)
        print(tabulate([['.' if x < 0 else self._player_names[x] for x in row]
                        for row in self._state],
                       headers=range(self._columns)))

    def next_step(self, player_id, column):
        y = self._rows - 1
        while self._state[y, column] >= 0:
            y -= 1
        # TODO: handle this case
        if y < 0:
            raise RuntimeError()
        self._state[y, column] = player_id
        return column, y

    def _check_direction(self, player_id, step_point, dx, dy):
        score = 1
        for way in [-1, 1]:
            x, y = step_point
            x = x + way * dx
            y = y + way * dy
            while 0 <= x < self._columns and \
                    0 <= y < self._rows and \
                    self._state[y, x] == player_id:
                score += 1
                x = x + way * dx
                y = y + way * dy
        return score >= CONNECT_NUMBER

    def check4win(self, player_id, step_point):
        for dx, dy in [
            (1, 0),  # horizontal
            (0, 1),  # vertical
            (1, -1),  # diagonal upper-right
            (1, 1),  # diagonal upper-left
                       ]:
            if self._check_direction(player_id, step_point, dx, dy):
                print(f'The winner is "{self._player_names[player_id]}"')
                return True

    @property
    def players_count(self):
        return self._players_count

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns


if __name__ == '__main__':
    board = Board()
    while True:
        for player_id in range(board.players_count):
            board.draw(player_id, 'step')
            step_column = int(input("enter column: "))
            step_point = board.next_step(player_id, step_column)
            if board.check4win(player_id, step_point):
                board.draw(player_id, 'win')
                sys.exit(0)
