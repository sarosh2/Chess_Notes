import chess
import chess.polyglot
from config import BLACK, WIDTH, OPENING_BOOK_PATHS, TEXT_X_OFFSET, ROW_OFFSET, MAX_MOVES_PER_COLUMN, COLUMN_OFFSET

# Example stats area
stats = []

def get_opening_info(board):
    """
    Retrieves a list of common moves from multiple opening books for the given board position.
    Each move will be shown only once, even if it appears in multiple books.

    :param board: chess.Board instance representing the current board state.
    :return: A tuple with a name of the book and list of unique moves.
    """
    opening_name = "Multiple Openings Book(s):"
    moves_info = set()  # Use a set to avoid duplicate moves

    try:
        # Loop through all opening books
        for book_path in OPENING_BOOK_PATHS:
            with chess.polyglot.open_reader(book_path) as reader:
                # Retrieve all moves for the position in this book
                for entry in reader.find_all(board):
                    move = board.san(entry.move)
                    moves_info.add(move)  # Add move to the set (duplicates will be ignored)

    except FileNotFoundError:
        opening_name = "One or more opening books not found"
    
    return opening_name, list(moves_info)

def draw_section(screen, board, font, y_offset_const):
    y_offset = y_offset_const
    """
    Draw the stats section on the screen, including the book name and common moves.

    :param screen: The pygame screen object.
    :param board: The current chess.Board object.
    :param font: The font used to render text.
    :param y_offset: The vertical offset for rendering.
    """
    opening_name, moves_info = get_opening_info(board)

    # Display the opening name
    opening_text = font.render(f"{opening_name}", True, BLACK)
    screen.blit(opening_text, (WIDTH + TEXT_X_OFFSET, y_offset))
    y_offset += ROW_OFFSET

    # Initialize column offset and maximum number of moves per column
    x_offset = WIDTH + TEXT_X_OFFSET
    max_moves_per_column = MAX_MOVES_PER_COLUMN - 1
    current_column = 0

    # Display moves, 7 moves per column
    for i, move in enumerate(moves_info):
        # Reset y_offset after every 7 moves and move to the next column
        if i > 0 and i % max_moves_per_column == 0:
            y_offset = y_offset_const + 40  # Reset y_offset
            current_column += 1  # Move to the next column
            x_offset += COLUMN_OFFSET  # Add some horizontal space between columns (adjust as needed)

        move_text = font.render(f"{move}", True, BLACK)
        screen.blit(move_text, (x_offset, y_offset))
        y_offset += ROW_OFFSET # Move down vertically for the next move