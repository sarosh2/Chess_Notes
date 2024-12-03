from config import BLACK, WIDTH

stats = ["This shall be the stats area"]

def draw_section(screen, font, y_offset):
    for stat in stats:
        stat_text = font.render(stat, True, BLACK)
        screen.blit(stat_text, (WIDTH + 20, y_offset))
        y_offset += 40