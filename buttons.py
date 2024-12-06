import pygame
from config import TAB_ACTIVE_COLOR, TAB_INACTIVE_COLOR, BORDER_THICKNESS

def draw_button(screen, text, x, y, width, height, font, selected_button):
    """Draw a button with the provided text and position."""

    color = TAB_INACTIVE_COLOR
    if selected_button == text:
        color = TAB_ACTIVE_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), BORDER_THICKNESS)  # Border

    label = font.render(text, True, (0, 0, 0))
    label_rect = label.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(label, label_rect)