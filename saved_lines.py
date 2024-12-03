from config import BLACK, WIDTH
notes = ["This will have saved_lines"]
def draw_section(screen, font, y_offset):
    for note in notes:
        note_text = font.render(note, True, BLACK)
        screen.blit(note_text, (WIDTH + 20, y_offset))
        y_offset += 40