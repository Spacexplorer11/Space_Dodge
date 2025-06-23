import time

import pygame
from classes.button import Button
from drawing.pause_menu.settings import settings_menu
from drawing.tutorial_and_information.keybindings import keybindings_screen
from drawing.tutorial_and_information.welcome import welcome_screen
from file_handling.constants_and_file_loading import (
    WINDOW, start_button_image, muteImage, unmuteImage, title_screen_background, settings_icon_frames, WIDTH, HEIGHT
)
from file_handling.utility import ref

# Initialise pygame & pygame.mixer
pygame.init()
pygame.mixer.init()


def _play_title_music():
    pygame.mixer.music.load(ref("assets/sounds/background_music/title_screen/title_screen_music.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)


def _create_buttons():
    muteSymbol = Button(muteImage, 50, 200)
    unmuteSymbol = Button(unmuteImage, 50, 200)
    startButton = Button(start_button_image, 350, 300)
    settingsButton = Button(settings_icon_frames, WIDTH - settings_icon_frames[1].get_width() - 10,
                            HEIGHT - settings_icon_frames[1].get_height())
    return startButton, muteSymbol, unmuteSymbol, settingsButton


def _draw_title_screen(mute, startButton, muteSymbol, unmuteSymbol, settingsButton):
    WINDOW.blit(title_screen_background, (0, 0))
    startButton.draw()
    if mute:
        WINDOW.blit(muteSymbol.image, muteSymbol.pos)
    else:
        WINDOW.blit(unmuteSymbol.image, unmuteSymbol.pos)
    settingsButton.draw()


def _handle_title_events(startButton, muteSymbol, unmuteSymbol, settingsButton, mute):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True, mute  # Will return False, 0.0, mute in main
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if startButton.clicked():
                pygame.mixer.music.stop()
                return True, mute
            elif muteSymbol.clicked() or unmuteSymbol.clicked():
                mute = not mute
                pygame.mixer.music.unpause() if not mute else pygame.mixer.music.pause()
            elif settingsButton.clicked():
                settings_menu(mute)
    return False, mute


# Draw the title screen
def draw_title(mute, firstTime):
    _play_title_music()
    startButton, muteSymbol, unmuteSymbol, settingsButton = _create_buttons()
    start = False

    while not start:
        time.sleep(3 / 1000)
        _draw_title_screen(mute, startButton, muteSymbol, unmuteSymbol, settingsButton)
        pygame.display.update()
        start, mute = _handle_title_events(startButton, muteSymbol, unmuteSymbol, settingsButton, mute)
        if start is True and pygame.event.peek(pygame.QUIT):
            return False, 0.0, mute

    if firstTime:
        return _handle_first_time_flow(mute)
    return True, time.time(), mute


def _handle_first_time_flow(mute):
    # Handle the first-time user experience with welcome screen and keybindings.
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, 0.0, mute
            if event.type == pygame.KEYDOWN:  # Simplified from 'elif' after 'return'
                running, startTime = keybindings_screen(4)
                return running, startTime, mute
        welcome_screen()
        time.sleep(1/60)  # Add frame-rate limiting to prevent excessive CPU usage
