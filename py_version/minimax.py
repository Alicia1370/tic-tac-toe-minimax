from math import inf as infinity
from random import choice
from random import seed as randomseed       # Paul Lu
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)

Name: Qinglin (Alicia) Cheng
CCID :1679590
CMPUT274, Fall 2020

Weekly Exercise 6: OO Minimax
"""


class basic():
    """
    A class to store basic values that all other classes can inherit from.
    Attributes:
    ----------
    HUMAN: int
        the value that represents human player
    CMOP: int
        the value that represents computer player

    Methods:
    ----------
    get_HUMAN():
        Get the value of HUMAN
    get_COMP():
        Get the value of COMP
    """
    def __init__(self,):
        """
        Parameter:
        ----------
        HUMAN: int
            the value that represents human player
        CMOP: int
            the value that represents computer player
        """
        self.HUMAN = -1
        self.COMP = +1

    def get_HUMAN(self):
        """Get the value of human.
        Return:
        ----------
        The value of human
        """
        return(self.HUMAN)

    def get_COMP(self):
        """Get the value of computer.
        Return:
        ----------
        The value of computer
        """
        return(self.COMP)

    def __str__(self):
        """Returns the informal string representation of an oject.
        Return:
        ----------
        A message that contains the attributes of the oject.
        """
        m = 'HUMAN = {}, COMP = {}'.format(self.get_HUMAN(), self.get_COMP())
        return(m)

    def __repr__(self):
        """Returns the official string representation of an oject.
        Return:
        ----------
        The id of the object
        """
        return str(id(self))


class state(basic):
    """A class used to represent a temporary state of a board.
    Attributes:
    ----------
    state: list
        the temporary state

    Methods:
    ----------
    get_state(:
        Get the temporary state
    """
    def __init__(self, state):
        """
        Parameter:
        ----------
        state: list
            the temporary state
        """
        super().__init__()
        self.state = state

    def get_state(self):
        """Get the temporary state.
        Return:
        ----------
        The temporary state
        """
        return(self.state)

    def evaluate(self):
        """
        Method to heuristic evaluation of state.
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if self.wins(self.get_COMP()):
            score = +1
        elif self.wins(self.get_HUMAN()):
            score = -1
        else:
            score = 0

        return score

    def wins(self, player):
        """
        This method tests if a specific player wins. Possibilities:
        * Three rows    [X X X] or [O O O]
        * Three cols    [X X X] or [O O O]
        * Two diagonals [X X X] or [O O O]
        :param player: a human or a computer
        :return: True if the player wins
        """
        state = self.get_state()
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False

    def game_over(self):
        """
        This method tests if the human or computer wins
        based on current state
        :return: True if the human or computer wins
        """
        return self.wins(self.get_HUMAN()) or self.wins(self.get_COMP())

    def empty_cells(self):
        """
        Each empty cell will be added into cells' list
        :return: a list of empty cells
        """
        cells = []

        for x, row in enumerate(self.get_state()):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def __str__(self):
        """Returns the informal string representation of an oject.
        Return:
        ----------
        A message that contains the attributes of the oject.
        """
        return 'state = ' + str(self.get_state())

    def __repr__(self):
        """Returns the official string representation of an oject.
        Return:
        ----------
        The id of the object
        """
        identity = 'The id is {}'.format(id(self))
        return identity


class board(basic):
    """A class used to represent a board of a game.
    Attributes:
    ----------
    board: list
        the board of current game

    Methods:
    ----------
    get_board():
        Get the board
    newstate(state):
        Create a temporary state of a board
    currentBoard():
        Create a temporary state based on current board
    board_depth():
        Find the depth of current board
    game_over():
        Test if there is a winner based on current board
    wins(player):
        Test if a specific player wins
    """
    def __init__(self):
        """
        Parameter:
        ----------
        board: list
            the board of current game
        """
        super().__init__()
        self.board = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]

    def get_board(self):
        """Get the board
        Return:
        ----------
        The board
        """
        return(self.board)

    def newstate(self, states):
        """Create a temporary state based on
        a board passed.
        Return:
        ------
        The temporary state
        """
        newstate = state(states)
        return(newstate)

    def currentBoard(self):
        """Create a temporary state based on current board.
        Return:
        ------
        The temporary state of current board
        """
        current_board = state(self.get_board())
        return(current_board)

    def board_depth(self):
        """Find the depth of current board.
        Return:
        ------
        The depth
        """
        depth = len(self.currentBoard().empty_cells())
        return depth

    def game_over(self):
        """This method invokes .game_over() in class 'state'
        and tests if the human or computer wins based on
        current situation on board.
        Return:
        True if the human or computer wins
        """
        return self.currentBoard().game_over()

    def wins(self, player):
        """This method invokes .wins() method in class 'state'
        and tests if a specific player wins based on current
        state of board.
        Parameter:
        ------
        player: a human or a computer

        Return:
        ------
        True if the player wins
        """
        return self.currentBoard().wins(player)

    def valid_move(self, x, y):
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the board[x][y] is empty
        """
        if [x, y] in self.currentBoard().empty_cells():
            return True
        else:
            return False

    def set_move(self, x, y, player):
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player: the current player
        """
        if self.valid_move(x, y):
            self.get_board()[x][y] = player
            return True
        else:
            return False

    def minimax(self, state, depth, player):
        """
        AI function that chooses the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """
        if player == self.get_COMP():
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        # Instantiate a new ojbect based on state passed
        newstate = self.newstate(state)

        # Invoke methods from state based on 'newstate'
        if depth == 0 or newstate.game_over():
            score = newstate.evaluate()
            return [-1, -1, score]

        for cell in newstate.empty_cells():
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, -player)

            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.get_COMP():
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def render(self, c_choice, h_choice):
        """
        Print the board on console
        :param state: current state of the board
        """
        chars = {
            -1: h_choice,
            +1: c_choice,
            0: ' '
        }

        str_line = '---------------'

        print('\n' + str_line)
        for row in self.get_board():
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)

    def ai_turn(self, c_choice, h_choice):
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = self.board_depth()
        if depth == 0 or self.game_over():
            return

        clean()
        print(f'Computer turn [{c_choice}]')
        self.render(c_choice, h_choice)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(self.get_board(), depth, self.get_COMP())
            x, y = move[0], move[1]

        self.set_move(x, y, self.get_COMP())
        # Paul Lu.  Go full speed.
        # time.sleep(1)

    def human_turn(self, c_choice, h_choice):
        """
        The Human plays choosing a valid move.
        :param c_choice: computer's choice X or O
        :param h_choice: human's choice X or O
        :return:
        """
        depth = self.board_depth()
        if depth == 0 or self.game_over():
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        clean()
        print(f'Human turn [{h_choice}]')
        self.render(c_choice, h_choice)

        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = self.set_move(coord[0], coord[1], self.get_HUMAN())

                if not can_move:
                    print('Bad move')
                    move = -1

            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

    def __str__(self):
        """Returns the informal string representation of an oject.
        Return:
        ----------
        A message that contains the attributes of the oject.
        """
        return 'board = ' + str(self.get_board())

    def __repr__(self):
        """Returns the official string representation of an oject.
        Return:
        ----------
        The id of the object
        """
        identity = 'The id is {}'.format(id(self))
        return identity


class choices():
    """A class used to represent choices of the game.
    Attributes:
    ----------
    h_choice: string
        the pattern of human choice
    C_choice: string
        the pattern of computer choice
    first: string
        the decision of who plays first

    Methods:
    ----------
    get_c_choice():
        Get the the pattern of human choice
    get_h_choice():
        Get the the pattern of computer choice
    get_first():
        Get the decision of who plays first
    choose_pattern():
        Set patterns for human and computer choices
    play_order():
        Set the order of who plays first
    """
    def __init__(self):
        """
        Parameter:
        ----------
        h_choice: string
            the pattern of human choice
        C_choice: string
            the pattern of computer choice
        first: string
            the decision of who plays first
        """
        self.h_choice = ''  # X or O
        self.c_choice = ''  # X or O
        self.first = ''  # if human is the first

    def get_c_choice(self):
        """Get computer choice.
        Return:
        ----------
        The computer choice
        """
        return(self.c_choice)

    def get_h_choice(self):
        """Get human choice.
        Return:
        ----------
        The human choice
        """
        return(self.h_choice)

    def get_first(self):
        """Get the decision of who plays first.
        Return:
        ----------
        The decision of who plays first
        """
        return(self.first)

    def choose_pattern(self):
        """Set patterns for human and computer choices.
        Return:
        ------
        None
        """
        # Human chooses X or O to play
        while self.h_choice != 'O' and self.h_choice != 'X':
            try:
                print('')
                self.h_choice = input('Choose X or O\nChosen: ').upper()

            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

        # Setting computer's choice
        if self.h_choice == 'X':
            self.c_choice = 'O'
        else:
            self.c_choice = 'X'

    def play_order(self):
        """Set the order of who plays first.
        Return:
        ------
        None
        """
        # Human may starts first
        while self.first != 'Y' and self.first != 'N':
            try:
                self.first = input('First to start?[y/n]: ').upper()

            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

    def __str__(self):
        """Returns the informal string representation of an oject.
        Return:
        ----------
        A message that contains the attributes of the oject.
        """
        m = 'human choice is [{}] and computer choice is [{}]'.format(
            self.get_h_choice, self.get_c_choice)

        return(m)

    def __repr__(self):
        """Returns the official string representation of an oject.
        Return:
        ----------
        The id of the object
        """
        identity = 'The id is {}'.format(id(self))
        return identity


def clean():
    """
    Clears the console
    """
    # Paul Lu.  Do not clear screen to keep output human readable.
    print()
    return

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def main():
    """
    Main function that calls all functions.
    """
    # Paul Lu.  Set the seed to get deterministic behaviour for each run.
    #       Makes it easier for testing and tracing for understanding.
    randomseed(274 + 2020)
    clean()

    # Create an object for first choice
    choice = choices()

    # Set patterns for human and computer choices
    choice.choose_pattern()
    c_choice = choice.get_c_choice()
    h_choice = choice.get_h_choice()
    clean()

    # Set the order of who plays first
    choice.play_order()
    first = choice.get_first()

    # Create a board for one turn of game
    board1 = board()

    # Main loop of this game
    while board1.board_depth() > 0 and not board1.game_over():
        if first == 'N':
            board1.ai_turn(c_choice, h_choice)
            first = ''

        board1.human_turn(c_choice, h_choice)
        board1.ai_turn(c_choice, h_choice)

    # Get the value of human and the value of computer
    HUMAN, COMP = board1.get_HUMAN(), board1.get_COMP()

    # Game over message
    if board1.wins(HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        board1.render(c_choice, h_choice)
        print('YOU WIN!')
    elif board1.wins(COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        board1.render(c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        board1.render(c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
