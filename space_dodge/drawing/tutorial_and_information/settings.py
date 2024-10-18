import time

import pygame

from space_dodge.classes.button import Button
from space_dodge.file_handling.constants_and_file_loading import (
    WINDOW, pause_background, muteImage, unmuteImage)
from space_dodge.file_handling.utility import ref

mutePauseSymbol = Button(pygame.transform.scale(muteImage, (120, 80)), 180, 430)
unmutePauseSymbol = Button(pygame.transform.scale(unmuteImage, (120, 80)), 180, 430)


def settings_menu(mute, pausedTimes):
    pygame.mixer.music.load(ref("sounds/background_music/pause_screen/pause_music.mp3"))
    pygame.mixer.music.play(-1)
    pauseStartTime = time.time()
    pause = True

    while pause:
        WINDOW.blit(pause_background, (0, 0))
        WINDOW.blit(mutePauseSymbol.image if mute else unmutePauseSymbol.image, (180, 430))
        pygame.mixer.music.pause() if mute else pygame.mixer.music.unpause()

        pausedTime = time.time() - pauseStartTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, pause, 0.0
            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m] or (unmutePauseSymbol.rect.collidepoint(pygame.mouse.get_pos())
                                        or mutePauseSymbol.rect.collidepoint(pygame.mouse.get_pos())):
                    mute = not mute
                elif keys[pygame.K_p] or keys[pygame.K_ESCAPE]:
                    pausedTimes.append(round(pausedTime))
                    totalPausedTime = sum(pausedTimes)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(ref("sounds/background_music/background_music.mp3"))
                    pygame.mixer.music.play(-1)
                    return True, pause, totalPausedTime

        pygame.display.update()
