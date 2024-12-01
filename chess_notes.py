import pygame
import chess
from board import draw_board
from piece import draw_pieces, load_images
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

# Initialize Pygame
pygame.init()

# Constants for the board
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Notes")

def main():
    clock = pygame.time.Clock()
    board = chess.Board()

    # Load images (called once at the start)
    load_images(SQUARE_SIZE)

    dragging_piece = None  # The piece being dragged
    original_square = None  # The original position of the piece
    offset_x, offset_y = 0, 0  # Offset for mouse dragging
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col, row = mouse_x // SQUARE_SIZE, (HEIGHT - mouse_y) // SQUARE_SIZE

                piece = board.piece_at(chess.square(col, row))
                if piece:
                    # If a piece is clicked, start dragging it
                    dragging_piece = piece
                    original_square = chess.square(col, row)
                    offset_x, offset_y = mouse_x - col * SQUARE_SIZE, mouse_y - (HEIGHT - row * SQUARE_SIZE)

            if event.type == MOUSEMOTION:
                if dragging_piece:
                    # If dragging, update the position of the piece
                    mouse_x, mouse_y = event.pos
                    offset_x, offset_y = mouse_x - (original_square % 8) * SQUARE_SIZE, mouse_y - (HEIGHT - (original_square // 8) * SQUARE_SIZE)

            if event.type == MOUSEBUTTONUP:
                if dragging_piece:
                    # Check if the move is legal
                    mouse_x, mouse_y = event.pos
                    col, row = mouse_x // SQUARE_SIZE, (HEIGHT - mouse_y) // SQUARE_SIZE
                    target_square = chess.square(col, row)
                    
                    # Make the move if it's legal
                    if board.is_legal(chess.Move(original_square, target_square)):
                        board.push(chess.Move(original_square, target_square))
                    # Reset dragging
                    dragging_piece = None
                    original_square = None

        draw_board(screen, WIDTH, HEIGHT, SQUARE_SIZE)  # Draw the board
        draw_pieces(screen, board, SQUARE_SIZE, dragging_piece, original_square, offset_x, offset_y)  # Draw the pieces with drag offset
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
