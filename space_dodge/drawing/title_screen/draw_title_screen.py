import pygame

from space_dodge.drawing.tutorial_and_information.keybindings import keybindings_screen
from space_dodge.drawing.tutorial_and_information.welcome import welcome_screen
from space_dodge.file_handling.constants_and_file_loading import (
    WINDOW, WIDTH, HEIGHT, start_button_image, muteImage, unmuteImage, title_screen_image
)
from space_dodge.file_handling.utility import ref

# Initialise pygame & pygame.mixer
pygame.init()
pygame.mixer.init()

# Define Rect objects
start_button_rect = start_button_image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
muteSymbol_rect = muteImage.get_rect(x=50, y=200, width=80, height=60)
unmuteSymbol_rect = unmuteImage.get_rect(x=50, y=200, width=80, height=60)


# Draw the title screen
def draw_title():
    # Load the title screen music
    pygame.mixer.music.load(ref("sounds/background_music/title_screen/title_screen_music.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
    mute = False
    start = False

    while not start:
        WINDOW.blit(title_screen_image, (0, 0))
        WINDOW.blit(start_button_image, start_button_rect.topleft)
        WINDOW.blit(muteImage if mute else unmuteImage, (50, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    start = True
                    pygame.mixer.music.stop()
                elif muteSymbol_rect.collidepoint(mouse_x, mouse_y) or unmuteSymbol_rect.collidepoint(mouse_x, mouse_y):
                    mute = not mute
                    pygame.mixer.music.unpause() if not mute else pygame.mixer.music.pause()

        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                startTime, info_screen_active, keyPress = keybindings_screen(None)
                return startTime, info_screen_active, keyPress
        welcome_screen()
