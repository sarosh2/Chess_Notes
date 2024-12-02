# move_history.py

import pygame
from config import WIDTH, NOTES_WIDTH, TAB_HEIGHT

def draw_move_history(screen, font, width, height, board):
    """Draw the move history section under 'Move History'."""
    # Draw "Move History" title
    
    
    move_history_title = font.render("Move History", True, (0, 0, 0))
    move_history_title_width = move_history_title.get_width()
    pygame.draw.rect(screen, (150, 150, 150), (WIDTH, height, width, TAB_HEIGHT))
    pygame.draw.rect(screen, (0, 0, 0), (WIDTH, height, width, TAB_HEIGHT), 2)  # Border of the tab
    
    screen.blit(move_history_title, (WIDTH + (NOTES_WIDTH - move_history_title_width) // 2, height + (TAB_HEIGHT - move_history_title.get_height()) // 2))  # Center the title

    # Define offsets and section widths
    left_x = WIDTH + 20  # Left side (White moves)
    right_x = WIDTH + NOTES_WIDTH // 2 + 20  # Right side (Black moves)
    y_offset = height + 50  # Start below the title

    # Split moves into White's and Black's moves
    white_moves = []  # Store white's moves
    black_moves = []  # Store black's moves

    for move_num, move in enumerate(board.move_stack, start=1):
        # Alternate moves between White and Black
        if move_num % 2 == 1:  # White's move (odd-numbered moves)
            white_moves.append(str(move))
        else:  # Black's move (even-numbered moves)
            black_moves.append(str(move))

    # Draw White's moves on the left half
    for i, move in enumerate(white_moves):
        move_text = font.render(f"{i + 1}. {move}", True, (0, 0, 0))
        screen.blit(move_text, (left_x, y_offset))
        y_offset += 30  # Add space between moves

    # Reset y_offset for the right side (Black's moves)
    y_offset = height + 50

    # Draw Black's moves on the right half
    for i, move in enumerate(black_moves):
        move_text = font.render(f"{move}", True, (0, 0, 0))
        screen.blit(move_text, (right_x, y_offset))
        y_offset += 30  # Add space between moves
