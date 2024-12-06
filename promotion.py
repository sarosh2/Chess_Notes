import pygame
import chess
from config import TAB_ACTIVE_COLOR, BLACK, WHITE, SQUARE_SIZE, PIECE_IMAGES

def show_promotion_dialog(screen, color, column, row):
    """
    Display a promotion dialog box allowing the user to choose a piece.

    Parameters:
    - screen: Pygame display surface.

    Returns:
    - The chosen piece type (e.g., chess.QUEEN, chess.ROOK, etc.), or None if canceled.
    """
    if color == chess.WHITE:

        options = [
            (chess.QUEEN, PIECE_IMAGES["wq"]),
            (chess.KNIGHT, PIECE_IMAGES["wn"]),
            (chess.ROOK, PIECE_IMAGES["wr"]),
            (chess.BISHOP, PIECE_IMAGES["wb"]),
        ]

    else:

        options = [
            (chess.BISHOP, PIECE_IMAGES["bb"]),
            (chess.ROOK, PIECE_IMAGES["br"]),
            (chess.KNIGHT, PIECE_IMAGES["bn"]),
            (chess.QUEEN, PIECE_IMAGES["bq"]),
        ]

    dialog_width = SQUARE_SIZE
    dialog_height = SQUARE_SIZE * (len(options))  # Additional space for the cancel button
    dialog_x = column * SQUARE_SIZE
    dialog_y = (7 - row) * SQUARE_SIZE
    if color == chess.BLACK:
        dialog_y -= dialog_height - SQUARE_SIZE
    dialog_rect = pygame.Rect(dialog_x, dialog_y, dialog_width, dialog_height)

    button_height = dialog_height // (len(options))  # Adjust button height to include cancel button
    buttons = []
    for i, (piece, img) in enumerate(options):
        button_rect = pygame.Rect(dialog_x, dialog_y + i * button_height, dialog_width, button_height)
        buttons.append((button_rect, piece, img))

    # Add cancel button
    if color == chess.WHITE:
        cancel_button_rect = pygame.Rect(dialog_x, dialog_y + len(options) * button_height, dialog_width, button_height // 2)
    else:
        cancel_button_rect = pygame.Rect(dialog_x, dialog_y - button_height // 2, dialog_width, button_height // 2)

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
                if cancel_button_rect.collidepoint(mouse_x, mouse_y):
                    selected_piece = None
                    waiting = False
                    break

        # Draw dialog box
        screen.fill(WHITE, dialog_rect)  # White background

        # Draw buttons with images
        for button_rect, _, img in buttons:
            screen.blit(img, button_rect.topleft)

        # Draw cancel button
        pygame.draw.rect(screen, TAB_ACTIVE_COLOR, cancel_button_rect)  # Red background for cancel button
        font = pygame.font.Font(None, SQUARE_SIZE // 2)
        text = font.render("X", True, BLACK)
        text_rect = text.get_rect(center=cancel_button_rect.center)
        screen.blit(text, text_rect)

        pygame.display.flip()

    return selected_piece
