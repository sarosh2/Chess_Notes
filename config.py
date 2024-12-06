# Constants for the board
WIDTH, HEIGHT = 800, 800
NOTES_WIDTH = 600  # Width of the notes section
SQUARE_SIZE = WIDTH // 8
TAB_HEIGHT = 40
BUTTON_WIDTH = NOTES_WIDTH // 4
BORDER_THICKNESS = 2

BLACK = (0, 0, 0) #used for fonts and base app background
WHITE = (255, 255, 255) #Used for promotion dialog box

DARK_SQUARE_COLOR = (181, 136, 99)
LIGHT_SQUARE_COLOR = (240, 217, 181)
SIDELINE_DARK_SQUARE_COLOR = (160, 160, 120) 
SIDELINE_LIGHT_SQUARE_COLOR = (240, 230, 210)

#used for notes, tabs and buttons
BACKGROUND_COLOR = (240, 240, 240)
TAB_ACTIVE_COLOR = (150, 150, 150)
TAB_INACTIVE_COLOR = (220, 220, 220)
FONT_SIZE = 30
BOARD_LABEL_FONT_SIZE = 24
BOARD_FONT_STYLE = "Arial"

#Various Titles for notes, the app and the game
APP_TITLE = "Chess Notes"
GAME_TITLE = "Welcome To The Deep Dark Forest"
NOTES_TITLE = "My Notes"
MOVE_HISTORY_TITLE = "Move History"
TABS = ["Saved Lines", "Book Lines", "Engine Lines"]
BUTTONS = [""]

DRAW_INTERVAL = 1500  # 1.5 seconds in milliseconds to draw Engine lines once every interval

TEXT_Y_OFFSET = 100
TEXT_X_OFFSET = 20
MAX_MOVES_PER_COLUMN = 8
COLUMN_OFFSET = 200
ROW_OFFSET = 40

NOTES_FILE_PATH = "saved_lines/my_notes"
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

ENGINE_PATH = "engine\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe"

# Dictionary to store images for the pieces
PIECE_IMAGES = {}
