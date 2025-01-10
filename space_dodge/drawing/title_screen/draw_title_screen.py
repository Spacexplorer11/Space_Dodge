import pygame

from classes.button import Button
from drawing.tutorial_and_information.keybindings import keybindings_screen
from drawing.tutorial_and_information.settings import settings_menu
from drawing.tutorial_and_information.welcome import welcome_screen
from file_handling.constants_and_file_loading import (
    WINDOW, start_button_image, muteImage, unmuteImage, title_screen_background, settingsIcon, WIDTH, HEIGHT
)
from file_handling.utility import ref

# Initialise pygame & pygame.mixer
pygame.init()
pygame.mixer.init()


# Draw the title screen
def draw_title():
    # Load the title screen music
    pygame.mixer.music.load(ref("sounds/background_music/title_screen/title_screen_music.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)
    mute = False
    start = False

    # Define Button objects
    muteSymbol = Button(muteImage, 50, 200)
    unmuteSymbol = Button(unmuteImage, 50, 200)
    startButton = Button(start_button_image, 350, 300)
    settingsButton = Button(settingsIcon, WIDTH - settingsIcon.get_width() - 10,
                            HEIGHT - settingsIcon.get_height())

    while not start:
        WINDOW.blit(title_screen_background, (0, 0))
        WINDOW.blit(startButton.image, startButton.pos)
        if mute:
            WINDOW.blit(muteSymbol.image, muteSymbol.pos)
        else:
            WINDOW.blit(unmuteSymbol.image, unmuteSymbol.pos)
        WINDOW.blit(settingsButton.image, settingsButton.pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, 0.0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.clicked():
                    start = True
                    pygame.mixer.music.stop()
                elif muteSymbol.clicked() or unmuteSymbol.clicked():
                    mute = not mute
                    pygame.mixer.music.unpause() if not mute else pygame.mixer.music.pause()
                elif settingsButton.clicked():
                    settings_menu(mute, music_path="sounds/background_music/title_screen/title_screen_music.mp3")

        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, 0.0
            elif event.type == pygame.KEYDOWN:
                running, startTime = keybindings_screen(None)
                return running, startTime
        welcome_screen()
