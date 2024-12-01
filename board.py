import pygame

# Colors for the board
YELLOW = (240, 217, 181)  # #F0D9B5
BROWN = (181, 136, 99)    # #B58863

def draw_board(screen, WIDTH, HEIGHT, SQUARE_SIZE):
    """Draw the chessboard with alternating squares."""
    for row in range(8):
        for col in range(8):
            color = YELLOW if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
