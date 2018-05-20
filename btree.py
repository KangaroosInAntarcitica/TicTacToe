from board import Board
from node import Node


class BinaryNode(Node):
    MAX_CHILDREN = 2


class Tree:
    """
    BinaryTree, having the same functionality as Tree, but performing
    less computations and less precise (only 2 options)
    """
    def __init__(self):
        """
        initialise the tree (tree calculates 2 possible options till end)
        """
        self.board = Board()
        self.__root = BinaryNode(Board(), None, Board.PLAYER_1)
        self.player = Board.PLAYER_0
        self.win = False

    def move(self, position):
        """ Perform a move as a player """
        if self.win:
            raise ValueError('Game finished!')

        if self.board[position] != Board.CELL_EMPTY:
            raise ValueError('Cell not empty')

        self.board[position] = self.player
        self.__root = BinaryNode(self.board, position, self.player)

        self.change_player()

    def get_move(self):
        """ Get a move from computer """
        if self.__root.children is None:
            raise ValueError('Game has ended')

        children = [*sorted(self.__root.children, key=
                lambda x: x.win[0 if self.player == Board.PLAYER_0 else 1])]

        self.__root = children[-1]
        self.board[self.__root.position] = self.player
        self.change_player()

    def change_player(self):
        """ After move setup - player change and win calculations """
        if self.__root.children is None:
            if self.__root.win[0] == 1:
                self.win = Board.PLAYER_0
            elif self.__root.win[1] == 1:
                self.win = Board.PLAYER_1
            elif self.__root.win[0] == 0 and self.__root.win[1] == 0:
                self.win = 'tie'

        self.player = Board.PLAYERS[(Board.PLAYERS.index(self.player) + 1) %
                                   len(Board.PLAYERS)]
