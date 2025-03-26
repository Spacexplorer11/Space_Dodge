import pygame

from classes.button import Button
from drawing.pause_menu.settings import settings_menu
from file_handling.constants_and_file_loading import (
    WINDOW, PAUSE_FONT, PAUSE_FONT_SMALL, pause_background, muteImage, unmuteImage, pause_time, settings_icon_frames,
    x_button_icon)
from file_handling.utility import ref
import time

mutePauseButton = Button(pygame.transform.scale(muteImage, (120, 80)), 180, 430)
unmutePauseButton = Button(pygame.transform.scale(unmuteImage, (120, 80)), 180, 430)
settingsButton = Button(settings_icon_frames, 200, 180)  # Create the settings symbol object
xButton = Button(x_button_icon, 665, 176)  # Create the x button object


@pause_time
def pause_menu(score, elapsedTime, highscore, highscoreBreak, mute):
    pygame.mixer.music.load(ref("assets/sounds/background_music/pause_screen/pause_music.mp3"))
    pygame.mixer.music.play(-1)
    pause = True

    while pause:
        time.sleep(3 / 1000)
        WINDOW.blit(pause_background, (0, 0))
        WINDOW.blit(PAUSE_FONT.render("PAUSE MENU", 1, "white"), (290, 176))
        WINDOW.blit(PAUSE_FONT.render(f"Time played: {round(elapsedTime)} secs", 1, "white"), (180, 250))
        WINDOW.blit(PAUSE_FONT.render(f"Score: {score}", 1, "white"), (180, 310))
        WINDOW.blit(PAUSE_FONT_SMALL.render("Your high score", 1, "white"), (180, 370))
        highScoreText = PAUSE_FONT_SMALL.render(f" is {highscore}" if highscoreBreak else f" was {highscore}", 1,
                                                "white")
        settingsButton.draw()
        WINDOW.blit(highScoreText, (490, 370))
        WINDOW.blit(mutePauseButton.image if mute else unmutePauseButton.image, (180, 430))
        xButton.draw()

        pygame.mixer.music.pause() if mute else pygame.mixer.music.unpause()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, mute
            elif event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m] or unmutePauseButton.clicked() or mutePauseButton.clicked():
                    mute = not mute
                elif keys[pygame.K_ESCAPE] or xButton.clicked():
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    if not mute:
                        pygame.mixer.music.load(ref("assets/sounds/background_music/background_music.mp3"))
                        pygame.mixer.music.play(-1)
                    return True, mute
                elif settingsButton.clicked():
                    pause, mute = settings_menu(mute)

        pygame.display.update()
