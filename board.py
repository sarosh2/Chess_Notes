import pygame
from config import SQUARE_SIZE, WIDTH, HEIGHT
import chess
import tkinter as tk
from tkinter import filedialog

# Colors for the board
YELLOW = (240, 217, 181)  # #F0D9B5
BROWN = (181, 136, 99)    # #B58863
TEXT_COLOR_YELLOW = (240, 217, 181)
TEXT_COLOR_BROWN = (181, 136, 99)

def draw_board(screen, flip):
    """Draw the chessboard with alternating squares and labels."""
    font = pygame.font.SysFont('Arial', 24)  # You can adjust the font and size

    for row in range(8):
        for col in range(8):
            # Determine actual row and column based on flip
            display_row = 7 - row if flip else row
            display_col = 7 - col if flip else col

            # Determine square color
            color = YELLOW if (display_row + display_col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            # Label the ranks (1-8) on the left column (file 'a')
            if col == 0:
                text_color = TEXT_COLOR_BROWN if color == YELLOW else TEXT_COLOR_YELLOW
                rank_label = str(8 - display_row)  # Ranks are displayed in reverse order (8-1)
                text = font.render(rank_label, True, text_color)
                screen.blit(text, (col * SQUARE_SIZE + 5, row * SQUARE_SIZE + 5))  # Adjust position

            # Label the files (a-h) on the bottom row (rank 8)
            if row == 7:
                text_color = TEXT_COLOR_BROWN if color == YELLOW else TEXT_COLOR_YELLOW
                file_label = chr(97 + display_col)  # 'a' to 'h'
                text = font.render(file_label, True, text_color)
                screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE - text.get_width() - 5, row * SQUARE_SIZE + SQUARE_SIZE - text.get_height() - 5))  # Adjust position

def upload_pgn_dialog():
    import tkinter as tk
from tkinter import filedialog
import chess.pgn

def upload_pgn_dialog():
    # Hide the root tkinter window
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Bring the dialog to the front

    # Open file dialog to select the PGN file
    file_path = filedialog.askopenfilename(title="Select a PGN File", filetypes=[("PGN Files", "*.pgn")])

    # Check if the file is a valid PGN file
    if file_path.lower().endswith('.pgn'):
        try:
            # Read the PGN file using python-chess
            with open(file_path, "r") as pgn_file:
                game = chess.pgn.read_game(pgn_file)
            
            if game:
                print("PGN loaded successfully. Starting the game...")

                # Extract players' names and the result
                white_name = game.headers.get("White", "Unknown White")
                black_name = game.headers.get("Black", "Unknown Black")
                result = game.headers.get("Result", "Unknown result")

                # Format the result string
                result_str = f"{white_name} vs {black_name} {result}"


                board = game.board()

                # Apply the moves from the PGN game to the board
                for move in game.mainline_moves():
                    board.push(move)

                return result_str, board  # Return the loaded game object for further processing

        except Exception as e:
            print(f"Error loading PGN file: {e}")
            return None
    else:
        print("Selected file is not a valid PGN file.")
        return None
