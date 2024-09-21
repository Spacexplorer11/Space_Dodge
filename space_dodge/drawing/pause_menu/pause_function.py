import time

import pygame
import logging
from logging import getLogger

from space_dodge.drawing.exception_handling.draw_exception import draw_except
from space_dodge.file_handling.utility import ref

pygame.font.init()

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

logfile = ref('mylog.log')
logging.basicConfig(filename=logfile, level=logging.INFO)
logger = getLogger(__name__)

try:
    pause_background = pygame.transform.scale(pygame.image.load(ref("assets/pause_background.png")),
                                              (WIDTH, HEIGHT))
except FileNotFoundError:
    logger.exception('Pause background not found')  # log the exception in a file
    draw_except("Background")

# All the fonts
PAUSE_FONT = pygame.font.SysFont("Arial", 50)
PAUSE_FONT_SMALL = pygame.font.SysFont("Arial", 45)

try:
    mutePauseSymbol = pygame.transform.scale(pygame.image.load(ref("assets/mute.png")), (120, 80))
    unmutePauseSymbol = pygame.transform.scale(pygame.image.load(ref("assets/unmute.png")),
                                               (120, 80))
except FileNotFoundError:
    logger.exception("Mute/unmute symbol (pause) not found")  # log the exception in a file
    draw_except("Symbol")


def pause_menu(score, elapsedTime, highscore, highscoreBreak, mute, pausedTimes):
    pygame.mixer.music.load(ref("sounds/background_music/pause_screen/pause_music.mp3"))
    pygame.mixer.music.play(-1)
    pauseStartTime = time.time()
    pause = True
    while pause:
        WINDOW.blit(pause_background, (0, 0))
        pause_text = PAUSE_FONT.render("PAUSE MENU", 1, "white")
        timeText = PAUSE_FONT.render(f"Time played: {round(elapsedTime)} secs", 1, "white")
        scoreText = PAUSE_FONT.render(f"Score: {score}", 1, "white")
        highScoreTextPt1 = PAUSE_FONT_SMALL.render("Your high score", 1, "white")
        highScoreText_was = PAUSE_FONT_SMALL.render(f" was {highscore}", 1, "white")
        highScoreText_is = PAUSE_FONT_SMALL.render(f" is {highscore}", 1, "white")
        WINDOW.blit(pause_text, (290, 176))
        WINDOW.blit(timeText, (180, 250))
        WINDOW.blit(scoreText, (180, 310))
        # Check if the highscore is higher than the current score and if it is then say highscore "is" not "was"
        if highscoreBreak:
            WINDOW.blit(highScoreTextPt1, (180, 370))
            WINDOW.blit(highScoreText_is, (490, 370))
        else:
            WINDOW.blit(highScoreTextPt1, (180, 370))
            WINDOW.blit(highScoreText_was, (490, 370))
        if mute:
            WINDOW.blit(mutePauseSymbol, (180, 430))
            pygame.mixer.music.pause()
        else:
            WINDOW.blit(unmutePauseSymbol, (180, 430))
            pygame.mixer.music.unpause()

        mutePauseRect = mutePauseSymbol.get_rect(x=180, y=430)
        unmutePauseRect = unmutePauseSymbol.get_rect(x=180, y=430)
        pausedTime = time.time() - pauseStartTime
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                running = False
                return running, pause, 0.0
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m]:
                    mute = not mute
                elif keys[pygame.K_p] or keys[pygame.K_ESCAPE]:
                    pause = False
                    running = True
                    totalPausedTime = 0.0
                    pausedTimes.append(round(pausedTime))
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load(
                        ref("sounds/background_music/background_music.mp3"))
                    pygame.mixer.music.play(-1)
                    for num in pausedTimes:
                        totalPausedTime += num
                    return running, pause, totalPausedTime
                elif mutePauseRect.collidepoint(pygame.mouse.get_pos()) or unmutePauseRect.collidepoint(
                        pygame.mouse.get_pos()):
                    mute = not mute

        pygame.display.update()
