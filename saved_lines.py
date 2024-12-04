import os
import json
from chess import Board  # Assuming you're using python-chess for board handling
from config import BLACK, WIDTH

# Constants
NOTES_FILE_PATH = "saved_lines/my_notes"

# Function to load notes from file or create new if the file doesn't exist
def load_notes():
    if os.path.exists(NOTES_FILE_PATH):
        with open(NOTES_FILE_PATH, 'r') as file:
            return json.load(file)
    else:
        return {}

# Function to save notes back to the file
def save_notes(notes):
    with open(NOTES_FILE_PATH, 'w') as file:
        json.dump(notes, file)

# Initialize notes
notes = load_notes()

# Function to add a new note for a specific position (FEN)
def add_note_to_position(fen, san_move):
    if fen not in notes:
        notes[fen] = []
    if san_move not in notes[fen]:
        notes[fen].append(san_move)
        save_notes(notes)

def add_line_to_notes(moves):
    temp_board = Board()
    for move in moves:
        san_move = temp_board.san(move)
        fen = temp_board.fen()
        add_note_to_position(fen, san_move)
        temp_board.push(move)
    print("Saved New Line Successfully")

def delete_move(moves):

    if moves:
        temp_board = Board()
        for i in range(len(moves) - 1):
            temp_board.push(moves[i])
        move = moves[-1]
        fen = temp_board.fen()

        if fen in notes and temp_board.san(move) in notes[fen]:
            notes[fen].remove(temp_board.san(move))
            print("Move Deleted Successfully")
            save_notes(notes)

# Function to draw the section displaying the notes
def draw_section(screen, board, font, y_offset_const):
    # Convert the board's current position to FEN
    fen = board.fen()

    # Check if there's a note for this FEN
    if fen in notes:

        # Initialize column offset and maximum number of moves per column
        y_offset = y_offset_const
        x_offset = WIDTH + 20
        max_moves_per_column = 8
        current_column = 0

        for i, note in enumerate(notes[fen]):
            # Reset y_offset after every 7 moves and move to the next column
            if i > 0 and i % max_moves_per_column == 0:
                y_offset = y_offset_const  # Reset y_offset
                current_column += 1  # Move to the next column
                x_offset += 200  # Add some horizontal space between columns (adjust as needed)
            note_text = font.render(note, True, BLACK)
            screen.blit(note_text, (x_offset, y_offset))
            y_offset += 40
