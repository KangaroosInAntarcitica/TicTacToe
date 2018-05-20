from board import Board
from node import Node


class Tree:
    """
    The tree decides what to do based on the probability of each player
    wining, as specified in the nodes
    """
    def __init__(self):
        """
        initialise the tree (tree calculates all possible options)
        """
        self.board = Board()
        self.__root = Node(Board(), None, Board.PLAYER_1)
        self.current = self.__root
        self.player = Board.PLAYER_0
        self.win = False

    def move(self, position):
        """ Perform a move as a player """
        if self.current.children is None:
            raise ValueError('Game has ended')

        if self.board[position] != Board.CELL_EMPTY:
            raise ValueError('Cell not empty')

        for item in self.current.children:
            if item.position == position:
                self.current = item
                break

        self.change_player()

    def get_move(self):
        """ Get a move from computer """
        if self.current.children is None:
            raise ValueError('Game has ended')

        children = [*sorted(self.current.children, key=
                lambda x: x.win[0 if self.player == Board.PLAYER_0 else 1])]

        self.current = children[-1]
        self.change_player()

    def change_player(self):
        """ After move setup - player change and win calculations """
        if self.current.children is None:
            if self.current.win[0] == 1:
                self.win = Board.PLAYER_0
            elif self.current.win[1] == 1:
                self.win = Board.PLAYER_1
            elif self.current.win[0] == 0 and self.current.win[1] == 0:
                self.win = 'tie'

        self.board[self.current.position] = self.player
        self.player = Board.PLAYERS[(Board.PLAYERS.index(self.player) + 1) %
                                   len(Board.PLAYERS)]
