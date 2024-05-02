import tkinter as tk

class CheckersGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Checkers Game")
        
        # Create the game board
        self.create_board()

    def create_board(self):
        # Create a 2D list to store references to the label widgets representing the board squares
        self.board_labels = [[None for _ in range(8)] for _ in range(8)]
        
        # Create a frame to contain the board
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        # Loop to create labels for each square on the board
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                label = tk.Label(self.board_frame, bg=color, width=4, height=2)
                label.grid(row=row, column=col)
                self.board_labels[row][col] = label

    def run(self):
        self.root.mainloop()

# Create an instance of the CheckersGUI class and run the GUI
if __name__ == "__main__":
    game = CheckersGUI()
    game.run()
