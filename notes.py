import pygame
from config import WIDTH, HEIGHT, NOTES_WIDTH, TAB_HEIGHT, WHITE, BLACK, BACKGROUND_COLOR, TAB_ACTIVE_COLOR, TAB_INACTIVE_COLOR
from move_history import draw_move_history
import saved_lines
import stats
import engine

# Initialize Pygame font system explicitly
pygame.font.init()

# Font for notes
font = pygame.font.Font(None, 45)

# Initialize the selected tab to 'My Notes'
selected_tab = "Saved Lines"

def draw_notes(screen, board):
    """Draw the 'My Notes' section on the right side of the screen."""
    # Draw background for notes section
    pygame.draw.rect(screen, BACKGROUND_COLOR, (WIDTH, 0, NOTES_WIDTH, HEIGHT))  # Background
    pygame.draw.rect(screen, BLACK, (WIDTH, 0, NOTES_WIDTH, HEIGHT), 2)  # Border

    # Draw the title "My Notes" at the top, centered
    title_text = font.render("My Notes", True, BLACK)
    title_width = title_text.get_width()
    screen.blit(title_text, (WIDTH + (NOTES_WIDTH - title_width) // 2, 10))  # Position title at the top

    # Divide the section into two halves: top half for tabs and bottom half for Move History
    tab_width = NOTES_WIDTH // 3
    half_height = (HEIGHT - 50) // 2  # Adjust for the title's position

    # Draw the tab bar in the top half
    draw_tab(screen, WIDTH, 50, tab_width, TAB_HEIGHT, "Saved Lines", selected_tab == "Saved Lines", 0)
    draw_tab(screen, WIDTH + tab_width, 50, tab_width, TAB_HEIGHT, "Stats", selected_tab == "Stats", 1)
    draw_tab(screen, WIDTH + 2 * tab_width, 50, tab_width, TAB_HEIGHT, "Engine Lines", selected_tab == "Engine Lines", 2)

    # Draw "Move History" title in the bottom half
    draw_move_history(screen, font, tab_width * 3, half_height + 60, board)

    # Draw content based on the selected tab
    y_offset = 100
    if selected_tab == "Saved Lines":
        saved_lines.draw_section(screen, font, y_offset)
    elif selected_tab == "Stats":
        stats.draw_section(screen, font, y_offset)
    elif selected_tab == "Engine Lines":
        engine.draw_section(screen, board, font, y_offset)


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
    x -= WIDTH
    if 0 <= x < tab_width:
        selected_tab = "Saved Lines"
    elif tab_width <= x < 2 * tab_width:
        selected_tab = "Stats"
    elif 2 * tab_width <= x < 3 * tab_width:
        selected_tab = "Engine Lines"