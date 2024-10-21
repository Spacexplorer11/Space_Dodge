import time

import pygame
import pygame_widgets
import threading

from space_dodge.classes.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from space_dodge.file_handling.constants_and_file_loading import (
    WINDOW, pause_background, muteImage, unmuteImage, PAUSE_FONT)
from space_dodge.file_handling.utility import ref

mutePauseSymbol = Button(pygame.transform.scale(muteImage, (120, 80)), 180, 430)
unmutePauseSymbol = Button(pygame.transform.scale(unmuteImage, (120, 80)), 180, 430)
slider_title = pygame.font.SysFont("comicsans", 30).render("Volume", 1, (255, 255, 255))


def settings_menu(mute, pausedTimes):
    pygame.mixer.music.load(ref("sounds/background_music/pause_screen/pause_music.mp3"))
    pygame.mixer.music.play(-1)
    slider = Slider(WINDOW, 350, 400, 100, 30, min=0, max=100, initial=pygame.mixer.music.get_volume() * 100)
    output = TextBox(WINDOW, 500, 395, 75, 50, fontSize=30)

    output.disable()  # Act as label instead of textbox
    pauseStartTime = time.time()
    pause = True

    while pause:
        WINDOW.blit(pause_background, (0, 0))
        WINDOW.blit(PAUSE_FONT.render("SETTINGS MENU", 1, "white"), (250, 176))
        WINDOW.blit(mutePauseSymbol.image if mute else unmutePauseSymbol.image, (180, 430))
        pygame.mixer.music.pause() if mute else pygame.mixer.music.unpause()
        WINDOW.blit(slider_title, (200, 390))

        pausedTime = time.time() - pauseStartTime

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False, pause, 0.0
            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m] or (unmutePauseSymbol.rect.collidepoint(pygame.mouse.get_pos())
                                        or mutePauseSymbol.rect.collidepoint(pygame.mouse.get_pos())):
                    mute = not mute
                elif keys[pygame.K_ESCAPE]:
                    pausedTimes.append(round(pausedTime))
                    totalPausedTime = sum(pausedTimes)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(ref("sounds/background_music/background_music.mp3"))
                    pygame.mixer.music.play(-1)
                    return True, pause, totalPausedTime

        output.setText(slider.getValue())

        pygame_widgets.update(events)

        pygame.display.update()
        update_music = threading.Thread(target=update_volume, args=(slider.getValue() / 100,))
        update_music.start()


def update_volume(volume):
    pygame.mixer.music.set_volume(volume)
