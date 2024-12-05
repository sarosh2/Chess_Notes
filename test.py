import pygame
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    """Opens a file dialog box to select a file and returns the file path."""
    # Hide the root tkinter window
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Bring the dialog to the front

    # Open file dialog
    file_path = filedialog.askopenfilename(title="Select a File")
    return file_path

# Example usage with pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("File Upload Example")

    font = pygame.font.Font(None, 36)
    text = "Press 'U' to upload a file"
    running = True
    file_path = None

    while running:
        screen.fill((0, 0, 0))
        rendered_text = font.render(text, True, (255, 255, 255))
        screen.blit(rendered_text, (50, 130))

        if file_path:
            # Display the selected file path on the screen
            file_display = font.render(f"File: {file_path}", True, (255, 255, 255))
            screen.blit(file_display, (50, 180))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    file_path = open_file_dialog()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
