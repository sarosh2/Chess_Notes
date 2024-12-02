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

# List of promotion piece types
PROMOTION_PIECES = [chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT]
PROMOTION_TEXTS = ['Queen', 'Rook', 'Bishop', 'Knight']

# Function to handle promotion (present a selection screen)
def handle_promotion(board, square):
    # Display promotion options on the screen
    promotion_rects = []
    font = pygame.font.Font(None, 36)
    screen.fill((0, 0, 0, 0))  # Clear the screen (use a transparent fill for the promotion screen)

    # Create buttons for each promotion type
    for i, piece in enumerate(PROMOTION_PIECES):
        rect = pygame.Rect(WIDTH // 4 + (i * WIDTH // 5), HEIGHT // 2, WIDTH // 5, 50)
        pygame.draw.rect(screen, (200, 200, 200), rect)
        text_surface = font.render(PROMOTION_TEXTS[i], True, (0, 0, 0))
        screen.blit(text_surface, (rect.x + 10, rect.y + 10))
        promotion_rects.append(rect)

    pygame.display.flip()

    # Wait for a click to select the promotion piece
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i, rect in enumerate(promotion_rects):
                    if rect.collidepoint(mouse_x, mouse_y):
                        return PROMOTION_PIECES[i]  # Return the selected promotion piece

    return chess.QUEEN  # Default to Queen if nothing is selected

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
                    
                    move = chess.Move(original_square, target_square)
                    
                    # Check if the move is legal
                    if board.is_legal(move):
                        board.push(move)
                        
                        # Check if the move was a pawn promotion
                        piece = board.piece_at(target_square)
                        if piece and piece.piece_type == chess.PAWN:
                            # If the pawn reaches the 8th rank for white or 1st rank for black
                            if row == 0 or row == 7:
                                promotion_piece = handle_promotion(board, target_square)
                                # Promote the pawn to the selected piece
                                promotion_move = chess.Move(target_square, target_square)
                                promotion_move.promotion = promotion_piece
                                board.push(promotion_move)
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
