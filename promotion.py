import pygame
import chess

def show_promotion_dialog(screen, square_size, color, column, row):
    """
    Display a promotion dialog box allowing the user to choose a piece.

    Parameters:
    - screen: Pygame display surface.
    - square_size: Size of a single square on the chessboard.

    Returns:
    - The chosen piece type (e.g., chess.QUEEN, chess.ROOK, etc.).
    """
    if color == chess.WHITE:

        # Load piece images
        piece_images = {
            chess.QUEEN: pygame.image.load(f"assets/wq.png"),
            chess.ROOK: pygame.image.load(f"assets/wr.png"),
            chess.BISHOP: pygame.image.load(f"assets/wb.png"),
            chess.KNIGHT: pygame.image.load(f"assets/wn.png"),
        }

        # Resize images to fit the square size
        piece_images = {piece: pygame.transform.scale(img, (square_size, square_size)) for piece, img in piece_images.items()}


        options = [
            (chess.QUEEN, piece_images[chess.QUEEN]),
            (chess.KNIGHT, piece_images[chess.KNIGHT]),
            (chess.ROOK, piece_images[chess.ROOK]),
            (chess.BISHOP, piece_images[chess.BISHOP]),
        ]

    else:

        # Load piece images
        piece_images = {
            chess.QUEEN: pygame.image.load(f"assets/bq.png"),
            chess.ROOK: pygame.image.load(f"assets/br.png"),
            chess.BISHOP: pygame.image.load(f"assets/bb.png"),
            chess.KNIGHT: pygame.image.load(f"assets/bn.png"),
        }

        # Resize images to fit the square size
        piece_images = {piece: pygame.transform.scale(img, (square_size, square_size)) for piece, img in piece_images.items()}

        options = [
            (chess.BISHOP, piece_images[chess.BISHOP]),
            (chess.ROOK, piece_images[chess.ROOK]),
            (chess.KNIGHT, piece_images[chess.KNIGHT]),
            (chess.QUEEN, piece_images[chess.QUEEN]),
        ]

    dialog_width = square_size
    dialog_height = square_size * len(options)
    dialog_x = column * square_size
    dialog_y = (7 - row) * square_size
    if color == chess.BLACK:
        dialog_y-= dialog_height - square_size
    dialog_rect = pygame.Rect(dialog_x, dialog_y, dialog_width, dialog_height)

    button_height = dialog_height // len(options)
    buttons = []
    for i, (piece, img) in enumerate(options):
        button_rect = pygame.Rect(dialog_x, dialog_y + i * button_height, dialog_width, button_height)
        buttons.append((button_rect, piece, img))

    selected_piece = None
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for button_rect, piece, _ in buttons:
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        selected_piece = piece
                        waiting = False
                        break

        # Draw dialog box
        screen.fill((255, 255, 255), dialog_rect)  # White background
        pygame.draw.rect(screen, (0, 0, 0), dialog_rect, 2)  # Black border

        # Draw buttons with images
        for button_rect, _, img in buttons:
            screen.blit(img, button_rect.topleft)
            pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)  # Black border for each button

        pygame.display.flip()

    return selected_piece