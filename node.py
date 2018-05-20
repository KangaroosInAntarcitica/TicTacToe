from board import Board


class Node:
    MAX_CHILDREN = 9

    def __init__(self, board, position, current_player):
        """ Initialise the node """
        self.board = board
        self.position = position
        self.current_player = current_player
        # win has 2 floats from 0-1 - probability of wining
        self.win = [None, None]
        self.children = None

        self.calculate_prob()

    def calculate_prob(self):
        """ Calculate the probability of best-case wining for each player """
        win = self.board.is_won()
        if win == Board.CELL_0:
            self.win = [1, 0]
        elif win == Board.CELL_1:
            self.win = [0, 1]
        elif win == Board.CELL_EMPTY and self.board.is_full():
            self.win = [0, 0]
        else:
            self.new_children()

        # clear some memory
        self.board = None

    def new_children(self):
        """ Add children and recalculate probability accordingly """
        self.children = []
        player = Board.PLAYERS[(Board.PLAYERS.index(self.current_player) + 1)
                              % len(Board.PLAYERS)]

        children = 0
        for i in range(9):
            if self.board[i] == Board.CELL_EMPTY and \
                    children < self.MAX_CHILDREN:
                # create new node with board
                new_board = self.board.__copy__()
                new_board[i] = player
                self.children.append(self.__class__(new_board, i, player))

                children += 1

        if self.current_player == Board.PLAYER_0:
            self.win[1] = max(self.children, key=lambda x: x.win[1]).win[1]
            self.win[0] = sum(map(lambda x: x.win[0] / len(self.children), self.children))

        elif self.current_player == Board.PLAYER_1:
            self.win[0] = max(self.children, key=lambda x: x.win[0]).win[0]
            self.win[1] = sum(map(lambda x: x.win[1] / len(self.children), self.children))
