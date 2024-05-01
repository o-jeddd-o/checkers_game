from core_gameplay.board import Board
from core_gameplay.ai import AI

# Initialize the game board
board = Board()

# Initialize the AI player
ai_player = AI(depth=3)  # Adjust depth for desired difficulty

# Define constants for player IDs
HUMAN_PLAYER = 1
AI_PLAYER = 2

# Define function to switch players
def switch_player(current_player):
    """
    Switches the current player.
    Args:
        current_player (int): The ID of the current player.
    Returns:
        int: The ID of the next player.
    """
    return HUMAN_PLAYER if current_player == AI_PLAYER else AI_PLAYER

# Define function to get human player's move
def get_human_move():
    """
    Prompts the human player to input their move.
    Returns:
        tuple: The start position and end position of the move.
    """
    while True:
        try:
            start_pos = tuple(map(int, input("Enter the start position (row, col): ").split(',')))
            end_pos = tuple(map(int, input("Enter the end position (row, col): ").split(',')))
            if board.is_valid_move(start_pos, end_pos):
                return start_pos, end_pos
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid coordinates.")

# Define main game loop
def main():
    """
    Main function to run the game loop.
    """
    current_player = HUMAN_PLAYER  # Human player starts first
    game_over = False

    while not game_over:
        # Human player's turn
        if current_player == HUMAN_PLAYER:
            # Get human player's move
            start_pos, end_pos = get_human_move()

            # Update game board with human player's move
            if board.move_piece(start_pos, end_pos):
                # Check if the game is over
                game_over = board.is_game_over() or board.is_draw()
                if game_over:
                    break
            else:
                print("Invalid move. Please try again.")

        # AI player's turn
        else:
            # Get AI player's best move
            best_move = ai_player.get_best_move(board.board)

            # Update game board with AI player's move
            if board.move_piece(best_move[0], best_move[1]):
                # Check if the game is over
                game_over = board.is_game_over() or board.is_draw()
                if game_over:
                    break

        # Switch to next player
        current_player = switch_player(current_player)

# Run the main function if this file is executed
if __name__ == "__main__":
    main()
