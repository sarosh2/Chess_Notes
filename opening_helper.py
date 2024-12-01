import pygame
import chess
import chess.svg

# Initialize pygame
pygame.init()

# Define constants
SQUARE_SIZE = 80
WIDTH, HEIGHT = SQUARE_SIZE * 8, SQUARE_SIZE * 8
LIGHT_SQUARE_COLOR = (240, 217, 181)  # #F0D9B5
DARK_SQUARE_COLOR = (181, 136, 99)   # #B58863
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Load piece images
def load_images():
    pieces = ['bp', 'br', 'bn', 'bb', 'bq', 'bk', 'wp', 'wr', 'wn', 'wb', 'wq', 'wk']
    images = {}
    for piece in pieces:
        images[piece] = pygame.image.load(f"assets/{piece}.png")
    return images

images = load_images()

# Initialize chess board
board = chess.Board()

def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_SQUARE_COLOR if (row + col) % 2 == 0 else DARK_SQUARE_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for square in range(64):
        row, col = divmod(square, 8)
        piece = board.piece_at(square)
        if piece:
            piece_img = images[str(piece)]
            screen.blit(piece_img, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def get_square_under_mouse():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // SQUARE_SIZE
    row = mouse_y // SQUARE_SIZE
    return row * 8 + col

def handle_dragging():
    dragging = False
    selected_piece_square = None
    selected_piece = None
    offset_x, offset_y = 0, 0

    while True:
        screen.fill((255, 255, 255))
        draw_board()
        draw_pieces()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                square = get_square_under_mouse()
                piece = board.piece_at(square)
                
                if piece:
                    selected_piece_square = square
                    selected_piece = piece
                    offset_x, offset_y = pygame.mouse.get_pos()
                    offset_x -= (selected_piece_square % 8) * SQUARE_SIZE
                    offset_y -= (selected_piece_square // 8) * SQUARE_SIZE
                    dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    square = get_square_under_mouse()
                    if board.is_legal(chess.Move(selected_piece_square, square)):
                        board.push(chess.Move(selected_piece_square, square))
                    dragging = False
                    selected_piece_square = None
                    selected_piece = None

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    # Get new mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Redraw background, board, and pieces
                    screen.fill((255, 255, 255))
                    draw_board()
                    draw_pieces()
                    # Draw the selected piece on top of the squares while dragging
                    piece_img = images[str(selected_piece)]
                    screen.blit(piece_img, (mouse_x - offset_x, mouse_y - offset_y))

        pygame.display.flip()

def main():
    running = True
    while running:
        handle_dragging()

if __name__ == "__main__":
    main()
