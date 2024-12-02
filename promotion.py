import pygame
import chess

def show_promotion_dialog(screen, square_size, color):
    """
    Display a promotion dialog box allowing the user to choose a piece.

    Parameters:
    - screen: Pygame display surface.
    - square_size: Size of a single square on the chessboard.

    Returns:
    - The chosen piece type (e.g., chess.QUEEN, chess.ROOK, etc.).
    """
    # Load piece images
    piece_images = {
        chess.QUEEN: pygame.image.load(f"assets/{'w' if color == chess.WHITE else 'b'}q.png"),
        chess.ROOK: pygame.image.load(f"assets/{'w' if color == chess.WHITE else 'b'}r.png"),
        chess.BISHOP: pygame.image.load(f"assets/{'w' if color == chess.WHITE else 'b'}b.png"),
        chess.KNIGHT: pygame.image.load(f"assets/{'w' if color == chess.WHITE else 'b'}n.png"),
    }

    # Resize images to fit the square size
    piece_images = {piece: pygame.transform.scale(img, (square_size, square_size)) for piece, img in piece_images.items()}

    options = [
        (chess.QUEEN, piece_images[chess.QUEEN]),
        (chess.ROOK, piece_images[chess.ROOK]),
        (chess.BISHOP, piece_images[chess.BISHOP]),
        (chess.KNIGHT, piece_images[chess.KNIGHT]),
    ]

    dialog_width = square_size * len(options)
    dialog_height = square_size
    dialog_x = (screen.get_width() - dialog_width) // 2
    dialog_y = (screen.get_height() - dialog_height) // 2
    dialog_rect = pygame.Rect(dialog_x, dialog_y, dialog_width, dialog_height)

    button_width = dialog_width // len(options)
    buttons = []
    for i, (piece, img) in enumerate(options):
        button_rect = pygame.Rect(dialog_x + i * button_width, dialog_y, button_width, dialog_height)
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