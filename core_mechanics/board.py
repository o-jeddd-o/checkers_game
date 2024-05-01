import numpy as np

class Board:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        """
        Initializes the game board with pieces in their starting positions.
        Returns:
            np.ndarray: A 2D NumPy array representing the game board.
        """
        board = np.zeros((8, 8), dtype=int)
        # Place red checkers
        board[1::2, ::2] = 1
        board[0::2, 1::2] = 1
        # Place white checkers
        board[6::2, 1::2] = 2
        board[7::2, ::2] = 2
        return board

    def is_valid_move(self, start_pos, end_pos):
        """
        Checks if a move from start_pos to end_pos is valid.
        Args:
            start_pos (tuple): Starting position of the piece.
            end_pos (tuple): Ending position of the piece.
        Returns:
            bool: True if the move is valid, False otherwise.
        """
        # Implement logic to check if the move is valid
        pass

    def move_piece(self, start_pos, end_pos):
        """
        Moves a piece from start_pos to end_pos if the move is valid.
        Args:
            start_pos (tuple): Starting position of the piece.
            end_pos (tuple): Ending position of the piece.
        Returns:
            bool: True if the move is successful, False otherwise.
        """
        if self.is_valid_move(start_pos, end_pos):
            # Implement logic to move the piece
            # Update the board state accordingly
            pass
        else:
            print("Invalid move")
            return False
