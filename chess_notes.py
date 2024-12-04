import pygame
import chess
from board import draw_board
from piece import draw_pieces, load_images
from promotion import show_promotion_dialog
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
import notes  # Import the notes module
from config import WIDTH, NOTES_WIDTH, HEIGHT, SQUARE_SIZE, TAB_HEIGHT, BACKGROUND_COLOR, BLACK
from buttons import draw_button, handle_button_click

# Initialize Pygame
pygame.init()

pygame.font.init()

# Font for notes
font = pygame.font.Font(None, 35)

# Adjust the width of the screen to include space for notes
screen_width = WIDTH + NOTES_WIDTH
screen = pygame.display.set_mode((screen_width, HEIGHT + TAB_HEIGHT))
pygame.display.set_caption("Chess Notes")
temp_move_history = []

def main():
    clock = pygame.time.Clock()
    board = chess.Board()

    # Load images (called once at the start)
    load_images()

    dragging_piece = None  # The piece being dragged
    original_square = None  # The original position of the piece
    selected_button = None
    offset_x, offset_y = 0, 0  # Offset for mouse dragging
    update = True

    # Draw the title "My Notes" at the top, centered
    title_text = font.render("My Notes", True, BLACK)
    title_width = title_text.get_width()

    # Draw background for notes section
    pygame.draw.rect(screen, BACKGROUND_COLOR, (WIDTH, 0, NOTES_WIDTH, 50))  # Background
    pygame.draw.rect(screen, BLACK, (WIDTH, 0, NOTES_WIDTH, HEIGHT), 2)  # Border
    screen.blit(title_text, (WIDTH + (NOTES_WIDTH - title_width) // 2, 10))  # Position title at the top

    draw_button(screen, "Welcome To The Deep Dark Forest", 0, HEIGHT, WIDTH, TAB_HEIGHT, font, selected_button)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if mouse_x >= WIDTH:  # Only check if the click was in the notes section
                    if 0 < mouse_y - 50 < TAB_HEIGHT:
                        notes.handle_tab_click(mouse_x, mouse_y)
                        update = True
                    elif 0 < mouse_y - HEIGHT < TAB_HEIGHT:
                        x = mouse_x - WIDTH
                        width = NOTES_WIDTH // 4
                        if 0 < x < width:
                            selected_button = "<"
                        elif width < x < 2 * width:
                            selected_button = ">"
                        elif 2 * width < x < 3 * width:
                            selected_button = "Save Line"
                        elif 3 * width < x < NOTES_WIDTH:
                            selected_button = "Delete Line" 
                else:
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
                    if mouse_x < WIDTH - 40:
                        offset_x, offset_y = mouse_x - (original_square % 8) * SQUARE_SIZE, mouse_y - (HEIGHT - (original_square // 8) * SQUARE_SIZE)

            if event.type == MOUSEBUTTONUP:
                if selected_button != None:
                    if selected_button == "<" and board.move_stack:
                        temp_move_history.append(board.pop())
                        update = True
                    elif selected_button == ">" and temp_move_history:
                        board.push(temp_move_history.pop())
                        update = True
                    elif selected_button == "Save Line":
                        notes.saved_lines.add_line_to_notes(board.move_stack)
                    elif selected_button == "Delete Line":
                        notes.saved_lines.delete_move(board.move_stack)
                    selected_button = None
                if dragging_piece:
                    # Check if the move is legal
                    mouse_x, mouse_y = event.pos
                    if 0 < mouse_x < WIDTH and 0 < mouse_y < HEIGHT:
                        col, row = mouse_x // SQUARE_SIZE, (HEIGHT - mouse_y) // SQUARE_SIZE
                        target_square = chess.square(col, row)

                        # Make the move if it's legal
                        promotion_piece = None
                        if piece.symbol() == 'P' and board.turn == chess.WHITE and target_square // 8 == 7 or piece.symbol() == 'p' and board.turn == chess.BLACK and target_square // 8 == 0:
                            promotion_piece = show_promotion_dialog(screen, SQUARE_SIZE, piece.color, col, row)

                        if board.is_legal(chess.Move(original_square, target_square, promotion_piece)):
                            board.push(chess.Move(original_square, target_square, promotion_piece))
                            temp_move_history.clear()
                            update = True
                    # Reset dragging
                    dragging_piece = None
                    original_square = None

        draw_board(screen)  # Draw the board
        draw_pieces(screen, board, dragging_piece, original_square, offset_x, offset_y)  # Draw the pieces with drag offset
        notes.draw_notes(screen, board, font, update)  # Draw the notes section
        update = False

        draw_button(screen, "<", WIDTH, HEIGHT, NOTES_WIDTH // 4, TAB_HEIGHT, font, selected_button)
        draw_button(screen, ">", WIDTH + NOTES_WIDTH // 4, HEIGHT, NOTES_WIDTH // 4, TAB_HEIGHT, font, selected_button)
        draw_button(screen, "Save Line", WIDTH + NOTES_WIDTH // 2, HEIGHT, NOTES_WIDTH // 4, TAB_HEIGHT, font, selected_button)
        draw_button(screen, "Delete Move", WIDTH + NOTES_WIDTH * 3 // 4, HEIGHT, NOTES_WIDTH // 4, TAB_HEIGHT, font, selected_button)
        pygame.display.flip()

        clock.tick(60)

    notes.engine.quit_engine()
    pygame.quit()

if __name__ == "__main__":
    main()
