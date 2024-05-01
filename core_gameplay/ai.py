class AI:
    def __init__(self, depth):
        self.depth = depth

    def minimax(self, board, depth, maximizing_player, alpha, beta):
        # Base case: Check if depth is 0 or game is over
        if depth == 0 or game_over:
            return self.evaluate_board(board), None

        # Get possible moves for the current player
        moves = self.get_possible_moves(board)

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in moves:
                # Make the move on a copy of the board
                new_board = self.make_move(board, move)
                eval_score, _ = self.minimax(new_board, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval_score)
                if max_eval >= beta:
                    break
                alpha = max(alpha, max_eval)
                if max_eval == eval_score:
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in moves:
                # Make the move on a copy of the board
                new_board = self.make_move(board, move)
                eval_score, _ = self.minimax(new_board, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval_score)
                if min_eval <= alpha:
                    break
                beta = min(beta, min_eval)
                if min_eval == eval_score:
                    best_move = move
            return min_eval, best_move

    def evaluate_board(self, board):
        """
        Evaluates the current board state and assigns a score.
        Args:
            board (np.ndarray): The current game board.
        Returns:
            int: The evaluation score for the board state.
        """
        red_score = 0
        white_score = 0

        for row in range(8):
            for col in range(8):
                if board[row][col] == 1:  # Red piece
                    red_score += 1
                    if row == 7:  # Promoted to king
                        red_score += 1
                elif board[row][col] == 2:  # White piece
                    white_score += 1
                    if row == 0:  # Promoted to king
                        white_score += 1

        return red_score - white_score

    def get_best_move(self, board):
        """
        Finds the best move for the AI player using the minimax algorithm.
        Args:
            board (np.ndarray): The current game board.
        Returns:
            tuple: The best move coordinates (start_pos, end_pos).
        """
        _, best_move = self.minimax(board, self.depth, True, float('-inf'), float('inf'))
        return best_move