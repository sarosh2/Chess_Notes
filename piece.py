import pygame
import chess

# Dictionary to store images for the pieces
PIECE_IMAGES = {}

def load_images(SQUARE_SIZE):
    """Load all chess piece images."""
    global PIECE_IMAGES
    for piece in ['bp', 'br', 'bn', 'bb', 'bq', 'bk', 'wp', 'wr', 'wn', 'wb', 'wq', 'wk']:
        try:
            PIECE_IMAGES[piece] = pygame.image.load(f"assets/{piece}.png")
            PIECE_IMAGES[piece] = pygame.transform.scale(PIECE_IMAGES[piece], (SQUARE_SIZE, SQUARE_SIZE))
            print(f"Loaded image for {piece}")
        except pygame.error:
            print(f"Failed to load image for {piece}")

def draw_pieces(screen, board, SQUARE_SIZE, dragging_piece=None, dragging_square=None, offset_x=0, offset_y=0):
    """Draw all the pieces on the board, with support for dragging."""
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)  # Flip row for pygame drawing
            # Use 'w' or 'b' for white or black, followed by the piece symbol (lowercase for black, uppercase for white)
            piece_color = 'w' if piece.color == chess.WHITE else 'b'
            piece_image_key = f"{piece_color}{piece.symbol().lower()}"
            piece_image = PIECE_IMAGES.get(piece_image_key)

            if piece_image:
                # Check if this piece is the one being dragged
                if piece == dragging_piece and dragging_square == square:
                    # Draw the piece with offset when dragging
                    screen.blit(piece_image, (offset_x + col * SQUARE_SIZE - SQUARE_SIZE // 2, offset_y + row * SQUARE_SIZE + SQUARE_SIZE // 2))
                else:
                    # Draw the piece normally on the board
                    screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            else:
                print(f"Missing image for {piece_image_key}")  # Debugging line
