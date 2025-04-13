import threading

import pygame
import pygame_widgets
import time

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from classes.button import Button
from file_handling.constants_and_file_loading import (
    WINDOW, pause_background, muteImage, unmuteImage, PAUSE_FONT, pause_time, x_button_icon)

mutePauseButton = Button(pygame.transform.scale(muteImage, (120, 80)), 180, 430)
unmutePauseButton = Button(pygame.transform.scale(unmuteImage, (120, 80)), 180, 430)
slider_title = pygame.font.SysFont("comicsans", 30).render("Volume", 1, (255, 255, 255))
xButton = Button(x_button_icon, 665, 175)  # Create the x button object

# No @paused_time decorator needed here bevause paused time is recorded by the pause menu,
# which is this is inside, and pause time doesn't matter on the title screen


def settings_menu(mute):
    time.sleep(3 / 1000)
    slider = Slider(WINDOW, 350, 400, 100, 30, min=0, max=100, initial=pygame.mixer.music.get_volume() * 100)
    output = TextBox(WINDOW, 500, 395, 75, 50, fontSize=30)

    output.disable()  # Act as label instead of textbox
    pause = True

    while pause:
        time.sleep(6.5 / 1000)
        WINDOW.blit(pause_background, (0, 0))
        WINDOW.blit(PAUSE_FONT.render("SETTINGS MENU", 1, "white"), (250, 176))
        if mute or pygame.mixer.music.get_volume() == 0:
            mutePauseButton.draw()
        else:
            unmutePauseButton.draw()
        if pygame.mixer.music.get_busy() is False and mute is False:
            pygame.mixer.music.load("assets/sounds/background_music/pause_screen/pause_music.mp3")
            pygame.mixer.music.play(-1)
        if pygame.mixer.music.get_volume() == 0:
            mute = True
            pygame.mixer.music.pause()
        WINDOW.blit(slider_title, (200, 390))
        xButton.draw()
        slider.draw()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False, mute
            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m] or unmutePauseButton.clicked() or mutePauseButton.clicked():
                    mute = not mute
                    pygame.mixer.music.pause() if mute else pygame.mixer.music.unpause()
                elif keys[pygame.K_ESCAPE] or xButton.clicked():
                    return pause, mute

        slider.listen(events)
        output.setText(slider.getValue())

        pygame_widgets.update(events)

        pygame.display.update()
        update_music = threading.Thread(target=update_volume, args=(slider.getValue() / 100,))
        update_music.start()


def update_volume(volume):
    pygame.mixer.music.set_volume(volume)
