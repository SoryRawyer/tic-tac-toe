"""
tictactoe.py - play tic tac toe from the command line
in the future, have the user input the number of games they'd like to play
and print out their record for that session

Tic-Tac-Toe board:
-+-+-
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9
-+-+-
"""

from __future__ import print_function
import random

class TicTacToe(object):
    """A class for a TicTacToe game"""

    winning_positions = [
        [0, 1, 2,],
        [3, 4, 5,],
        [6, 7, 8,],
        [0, 3, 6,],
        [1, 4, 7,],
        [2, 5, 8,],
        [0, 4, 8,],
        [2, 4, 6,],
    ]

    def __init__(self, user_symbol):
        self._board = [' '] * 9
        self._available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
        self._computer_symbol = 'X'
        self._user_symbol = input('Please enter a symbol to use (can either be X or O):')
        while self._user_symbol not in ('X', 'O'):
            self._user_symbol = input('Your symbol MUST be either upper-case X or upper-case O')
        if self._user_symbol == 'X':
            self._computer_symbol = 'O'
        self._outcome = ''

    def play(self):
        """
        play - play the game!
        accept user input
        validate moves (e.g. - make sure that tile's not already taken)
        end the game when someone wins or there are no more available moves
        """
        self._print_tutorial()
        while True:
            # get user move from input; set the board to their symbol
            # check if user won
            # if no more available moves, game ends in a draw
            # play the computer's move
            # check if computer won
            # if no more available moves, game ends in a draw
            self._play_user_move()
            if self._user_won():
                self._outcome = 'Congratulations, you won!'
                break
            if not self._available_moves:
                self._outcome = 'It\'s a draw!'
                break
            self._play_computer_move()
            if self._computer_won():
                self._outcome = 'Oh no, the computer won! Better luck next time!'
                break
            if not self._available_moves:
                self._outcome = 'It\'s a draw!'
                break
            print(TicTacToe.render_board(self._board))
        print(TicTacToe.render_board(self._board))
        print(self._outcome)
        return

    @staticmethod
    def render_board(tiles):
        """
        board - return the correct board to print out by formatting a template with stuff
        """
        if len(tiles) != 9:
            print(tiles)
            raise Exception('Excuse me, but you need all 9 tiles filled out (or\
            initialized as empty)')
        board_str = '-+-+-\n'
        for i in range(0, 9, 3):
            board_str += '|'.join(tiles[i:i+3])
            board_str += '\n'
            board_str += '-+-+-'
            board_str += '\n'
        return board_str

    def _won(self, tiles, symbol):
        """
        won - given the tiles and the symbol, check the winning positions to see
        if the given symbol won
        """
        won = False
        for i in TicTacToe.winning_positions:
            x, y, z = i
            won = won or (tiles[x] == symbol and tiles[y] == symbol and tiles[z] == symbol)
        return won

    def _user_won(self):
        """
        _user_won - did the user win this game?
        """
        return self._won(self._board, self._user_symbol)

    def _computer_won(self):
        """
        _computer_won - did the computer win this game?
        """
        return self._won(self._board, self._computer_symbol)

    def _print_tutorial(self):
        """
        _print_tutorial - print the tutorial board instructing users how to play
        """
        print('Welcome to Tic-Tac-Toe! To make a move, please enter the \
        number corresponding to the tile you\'d like to occupy')
        print(TicTacToe.render_board([str(x) for x in self._available_moves]))

    def _play_computer_move(self):
        """
        _play_computer_move - pick a random move from the available tiles
        """
        computer_move = random.choice(self._available_moves)
        self._board[computer_move - 1] = self._computer_symbol
        self._available_moves.remove(computer_move)
        return

    def _play_user_move(self):
        """
        _play_user_move - get user input from the command line, set their move on the board
        """
        player_move = input('Enter a number for your move:')
        while int(player_move) not in self._available_moves:
            print('Sorry, that tile is already occupied. Please select a new tile!')
            player_move = input('Enter a number for your move:')
        self._board[int(player_move) - 1] = self._user_symbol
        self._available_moves.remove(int(player_move))
        return


def main():
    """
    main - play tic tac toe
    """
    tic_tac_toe = TicTacToe('X')
    tic_tac_toe.play()
    return

if __name__ == '__main__':
    main()
