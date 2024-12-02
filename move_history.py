# move_history.py

import pygame

# Font for rendering moves
font = pygame.font.Font(None, 30)

def draw_move_history(screen, width, height, notes_width, board):
    """Draw the move history section under 'Move History'."""
    # Draw "Move History" title
    move_history_title = font.render("Move History", True, (0, 0, 0))
    move_history_title_width = move_history_title.get_width()
    screen.blit(move_history_title, (width + (notes_width - move_history_title_width) // 2, 100))  # Center the title

    # Draw the list of moves
    y_offset = 140  # Start below the title
    for move_num, move in enumerate(board.move_stack, start=1):
        move_text = font.render(f"{move_num}. {move}", True, (0, 0, 0))
        screen.blit(move_text, (width + 20, y_offset))
        y_offset += 30  # Add space between moves
