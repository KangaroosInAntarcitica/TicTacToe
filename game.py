from btree import Tree as BinaryTree
from tree import Tree


def perform_move(tree):
    """ Gets move input """
    while True:
        try:
            num = int(input('Your move (int 1-9):'))
            if 0 <= num - 1 < 9:
                tree.move(num - 1)
                break
            else:
                print('Invalid: not 0 < %s <= 9' % num)
        except ValueError as error:
            print(error)


def play():
    """ Main game """
    print('Please choose the bot version: ')
    print('0 - binary tree')
    print('1 - full version')
    tree = Tree if input('Choice: ') == '1' else BinaryTree
    tree = tree()

    print('\nPlease choose first player: ')
    print('x - you start')
    print('o - bot starts')
    player = 'o' if input('Choice: ') == 'o' else 'x'

    print('\nBoard indexing: \n+---+\n|123|\n|456|\n|789|\n+---+\n\n')

    if player == 'o':
        print(tree.board)
        tree.get_move()

    while not tree.win:
        print(tree.board)
        perform_move(tree)
        if not tree.win:
            print(tree.board)
            tree.get_move()

    print(tree.board)
    print('Won', tree.win)


if __name__ == '__main__':
    # run the program
    play()
