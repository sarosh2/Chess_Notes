import chess
import chess.polyglot
from config import BLACK, WIDTH

# List of paths to multiple Polyglot opening books
OPENING_BOOK_PATHS = [
    "openings\\polyglot-collection\\Book.bin",
    "openings\\polyglot-collection\\codekiddy.bin",
    "openings\\polyglot-collection\\DCbook_large.bin",
    "openings\\polyglot-collection\\Elo2400.bin",
    "openings\\polyglot-collection\\final-book.bin",
    "openings\\polyglot-collection\\gm2600.bin",
    "openings\\polyglot-collection\\komodo.bin",
    "openings\\polyglot-collection\\KomodoVariety.bin",
    "openings\\polyglot-collection\\Performance.bin",
    "openings\\polyglot-collection\\varied.bin",
    # Add more paths as needed
]

# Example stats area
stats = []

def get_opening_info(board):
    """
    Retrieves a list of common moves from multiple opening books for the given board position.
    Each move will be shown only once, even if it appears in multiple books.

    :param board: chess.Board instance representing the current board state.
    :return: A tuple with the opening name (static) and a list of unique moves.
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
    Draw the stats section on the screen, including the opening name and common moves.

    :param screen: The pygame screen object.
    :param board: The current chess.Board object.
    :param font: The font used to render text.
    :param y_offset: The vertical offset for rendering.
    """
    opening_name, moves_info = get_opening_info(board)

    # Display the opening name
    opening_text = font.render(f"{opening_name}", True, BLACK)
    screen.blit(opening_text, (WIDTH + 20, y_offset))
    y_offset += 40

    # Initialize column offset and maximum number of moves per column
    x_offset = WIDTH + 20
    max_moves_per_column = 7
    current_column = 0

    # Display moves, 7 moves per column
    for i, move in enumerate(moves_info):
        # Reset y_offset after every 7 moves and move to the next column
        if i > 0 and i % max_moves_per_column == 0:
            y_offset = y_offset_const + 40  # Reset y_offset
            current_column += 1  # Move to the next column
            x_offset += 200  # Add some horizontal space between columns (adjust as needed)

        move_text = font.render(f"{move}", True, BLACK)
        screen.blit(move_text, (x_offset, y_offset))
        y_offset += 40  # Move down vertically for the next move