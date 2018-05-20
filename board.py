class Board:
    CELL_EMPTY = ' '
    CELL_0 = 'x'
    CELL_1 = 'o'
    CELLS = (CELL_EMPTY, CELL_0, CELL_1)

    PLAYER_0 = 'x'
    PLAYER_1 = 'o'
    PLAYERS = [PLAYER_0, PLAYER_1]

    def __init__(self, values=None):
        """ Initialise a board """
        if values is None:
            values = self.CELL_EMPTY * 9
        if not all(map(lambda x: x in self.CELLS, values)):
            raise ValueError('One of the values is invalid')

        self.__values = [c for c in values]

    def __getitem__(self, i):
        """ Get one board item """
        if not (isinstance(i, int), 0 < i < 10):
            raise IndexError('Index should be 0 < int < 10, not %s' % i)
        return self.__values[i]

    def __setitem__(self, i, value):
        """ Set one board item """
        if not (isinstance(i, int), 0 < i < 10):
            raise IndexError('Index should be 0 < int < 10, not %s' % i)
        if value not in [self.CELL_EMPTY, self.CELL_0, self.CELL_1]:
            raise ValueError('Invalid cell value')
        self.__values[i] = value

    def __copy__(self):
        """ Copy a board """
        new_board = self.__class__()
        for i in range(0, 9):
            new_board[i] = self[i]
        return new_board

    def is_won(self):
        """ Returns if someone won the game """
        combinations = [*[(i, i + 3, i + 6) for i in range(3)],
                        *[(i*3, i*3 + 1, i*3 + 2) for i in range(3)],
                        (0, 4, 8), (2, 4, 6)]

        win = [*filter(lambda x: self[x[0]] == self[x[1]] == self[x[2]] and
                                 self[x[0]] != self.CELL_EMPTY, combinations)]
        return self[win[0][0]] if len(win) > 0 else self.CELL_EMPTY

    def is_full(self):
        """ Whether board is full """
        return all(map(lambda x: x != self.CELL_EMPTY, self.__values))

    def __repr__(self):
        """ Return a unique representation """
        result = ''
        for i in range(9):
            result += self[i]
        return result

    def __str__(self):
        """ Returns the board as a string """
        result = ''
        result += '+---+\n'
        for i in range(3):
            result += '|' + self[i*3] + self[i*3+1] + self[i*3+2] + '|\n'
        result += '+---+'
        return result
