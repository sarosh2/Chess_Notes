import pygame
from config import TAB_ACTIVE_COLOR, TAB_INACTIVE_COLOR

def draw_button(screen, text, x, y, width, height, font, selected_button):
    """Draw a button with the provided text and position."""

    color = TAB_INACTIVE_COLOR
    if selected_button == text:
        color = TAB_ACTIVE_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)  # Border

    label = font.render(text, True, (0, 0, 0))
    label_rect = label.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(label, label_rect)

def handle_button_click(mouse_x, mouse_y):
    """Handle clicks on the buttons below the notes section."""
    if BUTTON_Y_POS <= mouse_y <= BUTTON_Y_POS + BUTTON_HEIGHT:
        if 10 <= mouse_x <= 10 + BUTTON_WIDTH:
            # "<" Button: Pop from the board and add to the temp list
            if move_history:
                last_move = move_history.pop()
                temp_move_history.append(last_move)
                # Undo the move on the board
                board.pop()
        elif 10 + BUTTON_WIDTH <= mouse_x <= 10 + BUTTON_WIDTH * 2:
            # ">" Button: Pop from temp list and make the move
            if temp_move_history:
                last_temp_move = temp_move_history.pop()
                move_history.append(last_temp_move)
                board.push(last_temp_move)
        elif 10 + BUTTON_WIDTH * 2 <= mouse_x <= 10 + BUTTON_WIDTH * 3:
            # "Save Line" Button: Save the current move to the history
            if dragging_piece:
                move = chess.Move(original_square, target_square)
                move_history.append(move)
                board.push(move)
        elif 10 + BUTTON_WIDTH * 3 <= mouse_x <= 10 + BUTTON_WIDTH * 4:
            # "Delete Line" Button: Remove the last move from the move history
            if move_history:
                move_history.pop()
                board.pop()