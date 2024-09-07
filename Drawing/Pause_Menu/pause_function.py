import pygame
import logging
from logging import getLogger

from Drawing.Exception_Handling.draw_exception import draw_except
from File_Handling.Utility import ref

pygame.font.init()

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

logfile = ref('mylog.log')
logging.basicConfig(filename=logfile, level=logging.INFO)
logger = getLogger(__name__)


try:
    pause_background = pygame.transform.scale(pygame.image.load(ref("Assets/Pause_background.png")),
                                          (WIDTH, HEIGHT))
except FileNotFoundError:
    logger.exception('Pause background not found') # log the exception in a file
    error = "Background"
    draw_except(error)

# All the fonts
PAUSE_FONT = pygame.font.SysFont("Arial", 50)
PAUSE_FONT_SMALL = pygame.font.SysFont("Arial", 45)

try:
    mutePauseSymbol = pygame.transform.scale(pygame.image.load(ref("Assets/Mute.png")), (120, 80))
    unmutePauseSymbol = pygame.transform.scale(pygame.image.load(ref("Assets/Unmute.png")),
                                               (120, 80))
except FileNotFoundError:
    error = "Symbol"
    draw_except(error)


def pause_menu(score, elapsedTime, highscore, highscoreBreak, mute):
    WINDOW.blit(pause_background, (0, 0))
    pause_text = PAUSE_FONT.render("PAUSE MENU", 1, "white")
    timeText = PAUSE_FONT.render(f"Time played: {round(elapsedTime)} secs", 1, "white")
    scoreText = PAUSE_FONT.render(f"Score: {score}", 1, "white")
    highScoreTextPt1 = PAUSE_FONT_SMALL.render("Your high score", 1, "white")
    highScoreText_was = PAUSE_FONT_SMALL.render(f" was {highscore}", 1, "white")
    highScoreText_is = PAUSE_FONT_SMALL.render(f" is {highscore}", 1, "white")

    if mute:
        WINDOW.blit(mutePauseSymbol, (180, 430))
    else:
        WINDOW.blit(unmutePauseSymbol, (180, 430))
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

    pygame.display.update()
