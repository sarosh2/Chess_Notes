from config import BLACK, WIDTH

engine_lines = ["This will have engine lines"]

def draw_section(screen, font, y_offset):
    for line in engine_lines:
        line_text = font.render(line, True, BLACK)
        screen.blit(line_text, (WIDTH + 20, y_offset))
        y_offset += 40
