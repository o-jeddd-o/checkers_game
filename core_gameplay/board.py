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
        x1, y1 = start_pos
        x2, y2 = end_pos
        piece = self.board[x1][y1]

        # Check if end position is within bounds
        if x2 < 0 or x2 >= 8 or y2 < 0 or y2 >= 8:
            return False

        # Check if end position is empty
        if self.board[x2][y2] != 0:
            return False

        # Check if the move direction is valid for the piece
        if piece == 1:  # Red piece
            if x2 <= x1:
                return False
        elif piece == 2:  # White piece
            if x2 >= x1:
                return False

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
            x1, y1 = start_pos
            x2, y2 = end_pos
            piece = self.board[x1][y1]
            self.board[x1][y1] = 0  # Clear the start position
            self.board[x2][y2] = piece  # Move the piece to the end position
            return True
        else:
            print("Invalid move")
            return False

    def is_game_over(self):
        """
        Checks if the game is over by determining if one of the players has lost all their pieces.
        Returns:
            bool: True if the game is over, False otherwise.
        """
        red_pieces = np.count_nonzero(self.board == 1)
        white_pieces = np.count_nonzero(self.board == 2)
        return red_pieces == 0 or white_pieces == 0

    def is_draw(self):
        """
        Checks if the game is a draw by determining if there are no valid moves for either player.
        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        # Iterate through all pieces to check if any player has a valid move
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != 0:
                    piece = (row, col)
                    moves = self.get_possible_moves(piece)
                    if moves:
                        return False  # Found a valid move for a player
        return True  # No valid moves for either player, game is a draw