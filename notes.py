import pygame
from config import WIDTH, HEIGHT, NOTES_WIDTH

# Initialize Pygame font system explicitly
pygame.font.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (240, 240, 240)
TAB_ACTIVE_COLOR = (200, 200, 200)
TAB_INACTIVE_COLOR = (220, 220, 220)

# Font for notes
font = pygame.font.Font(None, 45)

# List to hold the notes
notes = []
stats = []
engine_lines = []

# Initialize the selected tab to 'My Notes'
selected_tab = "My Notes"

def draw_notes(screen):
    """Draw the 'My Notes' section on the right side of the screen."""
    # Draw background for notes section
    pygame.draw.rect(screen, BACKGROUND_COLOR, (WIDTH, 0, NOTES_WIDTH, HEIGHT))  # Background
    pygame.draw.rect(screen, BLACK, (WIDTH, 0, NOTES_WIDTH, HEIGHT), 2)  # Border

    # Draw the title "My Notes" at the top, centered
    title_text = font.render("My Notes", True, BLACK)
    title_width = title_text.get_width()
    screen.blit(title_text, (WIDTH + (NOTES_WIDTH - title_width) // 2, 10))  # Position title at the top

    # Divide the section into two halves: top half for tabs and bottom half for Move History
    tab_height = 40
    tab_width = NOTES_WIDTH // 3
    half_height = (HEIGHT - 50) // 2  # Adjust for the title's position

    # Draw the tab bar in the top half
    draw_tab(screen, WIDTH, 50, tab_width, tab_height, "Saved Lines", selected_tab == "My Notes", 0)
    draw_tab(screen, WIDTH + tab_width, 50, tab_width, tab_height, "Stats", selected_tab == "Stats", 1)
    draw_tab(screen, WIDTH + 2 * tab_width, 50, tab_width, tab_height, "Engine Lines", selected_tab == "Engine Lines", 2)

    # Draw "Move History" title in the bottom half
    move_history_title = font.render("Move History", True, BLACK)
    move_history_title_width = move_history_title.get_width()
    screen.blit(move_history_title, (WIDTH + (NOTES_WIDTH - move_history_title_width) // 2, half_height + 60))  # Center the title

    # Draw content based on the selected tab
    y_offset = half_height + 100  # Start below the "Move History" title
    if selected_tab == "My Notes":
        for note in notes:
            note_text = font.render(note, True, BLACK)
            screen.blit(note_text, (width + 20, y_offset))
            y_offset += 40
    elif selected_tab == "Stats":
        for stat in stats:
            stat_text = font.render(stat, True, BLACK)
            screen.blit(stat_text, (width + 20, y_offset))
            y_offset += 40
    elif selected_tab == "Engine Lines":
        for line in engine_lines:
            line_text = font.render(line, True, BLACK)
            screen.blit(line_text, (width + 20, y_offset))
            y_offset += 40


def draw_tab(screen, x, y, width, height, text, is_active, index):
    """Draw a tab on the screen."""
    color = TAB_ACTIVE_COLOR if is_active else TAB_INACTIVE_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)  # Border of the tab

    tab_text = font.render(text, True, BLACK)
    screen.blit(tab_text, (x + (width - tab_text.get_width()) // 2, y + (height - tab_text.get_height()) // 2))

def handle_tab_click(x, y):
    """Handle clicks to switch between tabs."""
    global selected_tab
    tab_width = NOTES_WIDTH // 3
    if 0 <= x < tab_width:
        selected_tab = "My Notes"
    elif tab_width <= x < 2 * tab_width:
        selected_tab = "Stats"
    elif 2 * tab_width <= x < 3 * tab_width:
        selected_tab = "Engine Lines"
