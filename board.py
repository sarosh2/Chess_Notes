import pygame
from config import SQUARE_SIZE, WIDTH, HEIGHT

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

