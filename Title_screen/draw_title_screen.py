import pygame
import os

from Exception_Handling.draw_exception import draw_except

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Button variables
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 200

# Initialise pygame mixer
pygame.mixer.init()

# Load the title screen image
try:
    title_screen_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Title_screen.jpg")), (WIDTH, HEIGHT))
except FileNotFoundError:
    error = "Background"
    draw_except(error)

# Load the start button image
try:
    start_button_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Start_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
except FileNotFoundError:
    error = "Button"
    draw_except(error)

# Check if the title screen music file exists
title_screen_music_check = os.path.exists(os.path.join("Sounds", "Background_music", "Title_screen", "Title_screen_music.mp3"))
if not title_screen_music_check:
    error = "Music"
    draw_except(error)

# Define Rect object for start button
start_button_rect = start_button_image.get_rect(x=WIDTH / 2 - BUTTON_WIDTH / 2, y=300)


# Draw the title screen
def draw_title(start, welcome):
    WINDOW.blit(title_screen_image, (0, 0))
    WINDOW.blit(start_button_image, (WIDTH / 2 - BUTTON_WIDTH / 2, 270))
    pygame.display.update()
    pygame.mixer.music.play(loops=-1)
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    start = True
                    welcome = True
                    return start, welcome
