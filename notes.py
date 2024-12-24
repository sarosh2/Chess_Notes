import pygame
from config import WIDTH, HEIGHT, NOTES_WIDTH, TAB_HEIGHT, BLACK, BACKGROUND_COLOR, TAB_ACTIVE_COLOR, TAB_INACTIVE_COLOR, NOTES_TITLE, TABS, DRAW_INTERVAL, TEXT_Y_OFFSET, BORDER_THICKNESS
from move_history import draw_move_history
import saved_lines
import stats
import engine

# Initialize the selected tab to 'My Notes'
selected_tab = TABS[0]

# Variable to track the last time content was drawn
last_draw_time = 0

def draw_title(screen, font):
    notes_title = font.render(NOTES_TITLE, True, BLACK)
    title_width = notes_title.get_width()
    title_height = notes_title.get_height()

    # Draw background for notes section
    pygame.draw.rect(screen, BACKGROUND_COLOR, (WIDTH, 0, NOTES_WIDTH, TAB_HEIGHT))  # Background
    pygame.draw.rect(screen, BLACK, (WIDTH, 0, NOTES_WIDTH, HEIGHT), BORDER_THICKNESS)  # Border
    screen.blit(notes_title, (WIDTH + (NOTES_WIDTH - title_width) // 2, (TAB_HEIGHT - title_height) // 2))  # Position title at the top

def draw_notes(screen, board, font, update, flip):
    """Draw the 'My Notes' section on the right side of the screen."""
    global last_draw_time

    # Divide the section into two halves: top half for tabs and bottom half for Move History
    tab_width = NOTES_WIDTH // 3
    half_height = (HEIGHT - 3 * TAB_HEIGHT) // 2 # Adjust for the title's and tabs's positions

    # Draw the tab bar in the top half
    if update:
        for i, tab in enumerate(TABS):
            draw_tab(screen, WIDTH + i * tab_width, TAB_HEIGHT, tab_width, TAB_HEIGHT, tab, selected_tab == tab, font)

        # Draw "Move History" title in the bottom half
        draw_move_history(screen, font, half_height + 2 * TAB_HEIGHT, board)

    # Get the current time in milliseconds
    current_time = pygame.time.get_ticks()

    # Draw content based on the selected tab
    y_offset = TEXT_Y_OFFSET
    if selected_tab == TABS[0] and update:
        pygame.draw.rect(screen, BACKGROUND_COLOR, (WIDTH, 2 * TAB_HEIGHT, NOTES_WIDTH, half_height))  # Background
        saved_lines.draw_section(screen, board, font, y_offset, flip)
    elif selected_tab == TABS[1] and update:
        pygame.draw.rect(screen, BACKGROUND_COLOR, (WIDTH, 2 * TAB_HEIGHT, NOTES_WIDTH, half_height))  # Background
        stats.draw_section(screen, board, font, y_offset)
    elif selected_tab == TABS[2] and current_time - last_draw_time >= DRAW_INTERVAL:
        # Update the last draw time
        last_draw_time = current_time
        pygame.draw.rect(screen, BACKGROUND_COLOR, (WIDTH, 2 * TAB_HEIGHT, NOTES_WIDTH, half_height))  # Background
        engine.draw_section(screen, board, font, y_offset)


def draw_tab(screen, x, y, width, height, text, is_active, font):
    """Draw a tab on the screen."""
    color = TAB_ACTIVE_COLOR if is_active else TAB_INACTIVE_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), BORDER_THICKNESS)  # Border of the tab

    tab_text = font.render(text, True, BLACK)
    screen.blit(tab_text, (x + (width - tab_text.get_width()) // 2, y + (height - tab_text.get_height()) // 2))

def handle_tab_click(x, y):
    """Handle clicks to switch between tabs."""
    global selected_tab
    tab_width = NOTES_WIDTH // 3
    x -= WIDTH
    if 0 <= x < tab_width:
        selected_tab = TABS[0]
    elif tab_width <= x < 2 * tab_width:
        selected_tab = TABS[1]
    elif 2 * tab_width <= x < 3 * tab_width:
        selected_tab = TABS[2]