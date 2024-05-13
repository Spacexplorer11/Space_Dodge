import pygame
import os

pygame.font.init()


# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pause_background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "pause_background.png")), (WIDTH, HEIGHT))

# All the fonts
PAUSE_FONT = pygame.font.SysFont("Arial", 50)
PAUSE_FONT_SMALL = pygame.font.SysFont("Arial", 48)


def pause_menu(score, elapsedTime, highscore, highscoreBreak):
    WINDOW.blit(pause_background, (0, 0))
    pause_text = PAUSE_FONT.render("PAUSE MENU", 1, "white")
    timeText = PAUSE_FONT.render(f"Time played: {round(elapsedTime)} secs", 1, "white")
    scoreText = PAUSE_FONT.render(f"Score: {score}", 1, "white")
    highScoreTextPt1 = PAUSE_FONT_SMALL.render(f"Your high score", 1, "white")
    highScoreText_was = PAUSE_FONT_SMALL.render(f" was {highscore}", 1, "white")
    highScoreText_is = PAUSE_FONT_SMALL.render(f" is {highscore}", 1, "white")
    WINDOW.blit(pause_text, (290, 176))
    WINDOW.blit(timeText, (180, 250))
    WINDOW.blit(scoreText, (180, 310))

    # Check if the highscore is higher than the current score and if it is then say highscore "is" not "was"
    if highscoreBreak:
        WINDOW.blit(highScoreTextPt1, (180, 370))
        WINDOW.blit(highScoreText_is, (510, 370))
    else:
        WINDOW.blit(highScoreTextPt1, (180, 370))
        WINDOW.blit(highScoreText_was, (510, 370))

    pygame.display.update()
