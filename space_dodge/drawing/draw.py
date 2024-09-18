import logging
from logging import getLogger

import pygame

from space_dodge.drawing.exception_handling.draw_exception import draw_except
from space_dodge.file_handling.utility import ref

logfile = ref('mylog.log')
logging.basicConfig(filename=logfile, level=logging.INFO)
logger = getLogger(__name__)

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Fonts
FONT = pygame.font.SysFont("Arial Black", 30)

# Player variables
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 80

# Bullet variables
BULLET_WIDTH = 50
BULLET_HEIGHT = 70

try:
    threeLives = pygame.transform.scale(pygame.image.load(ref("assets/three_lives.png")), (200, 200))
    twoLives = pygame.transform.scale(pygame.image.load(ref("assets/two_lives.png")), (200, 190))
    oneLife = pygame.transform.scale(pygame.image.load(ref("assets/one_life.png")), (200, 180))
except FileNotFoundError:
    logger.exception('Player not found')  # log the exception in a file
    draw_except("Lives")

try:
    Background = pygame.transform.scale(pygame.image.load(ref("assets/space_background.jpg")),
                                        (WIDTH, HEIGHT))
except FileNotFoundError:
    logger.exception('Background not found')  # log the exception in a file
    draw_except("Background")

try:
    pauseSymbol = pygame.transform.scale(pygame.image.load(ref("assets/pause_rectangle.png")), (50, 30))

except FileNotFoundError:
    logger.exception('Symbol not found') # log the exception in a file
    draw_except("Symbol")

try:
    bullet_texture = pygame.transform.scale(pygame.image.load(ref("assets/bullet_texture.png")), (BULLET_WIDTH, BULLET_HEIGHT))
except FileNotFoundError:
    logger.exception('Bullet texture not found') # log the exception in a file
    draw_except("Bullet")

# Create a mask for the bullet
bullet_mask = pygame.mask.from_surface(bullet_texture)


def draw(playerL, playerR, playerX, bullets, direction, highscore, highscoreBreak,
         mute, lives, muteSymbol, unmuteSymbol, timeText, scoreText):
    WINDOW.blit(Background, (0, 0))

    # Draw the bullets using the bullet surface
    for bullet in bullets:
        WINDOW.blit(bullet_texture, (bullet.x, bullet.y))

    highScoreTextPt1 = FONT.render(f"Your high score", 1, "white")
    highScoreText_was = FONT.render(f" was {highscore}", 1, "white")
    highScoreText_is = FONT.render(f" is {highscore}", 1, "white")

    WINDOW.blit(timeText, (10, 10))
    WINDOW.blit(scoreText, (WIDTH - 270, 10))
    WINDOW.blit(highScoreTextPt1, (250, 10))
    WINDOW.blit(pauseSymbol, (scoreText.get_width() + 745, 19))

    # Show the mute/unmute symbol
    if mute:
        WINDOW.blit(muteSymbol, (timeText.get_width() + 10, 10))
    else:
        WINDOW.blit(unmuteSymbol, (timeText.get_width() + 10, 10))

    # Check if the highscore is higher than the current score and if it is then say highscore "is" not "was"
    if highscoreBreak:
        WINDOW.blit(highScoreText_is, (500, 10))
    else:
        WINDOW.blit(highScoreText_was, (500, 10))

    # Changing where the player faces
    # 1 = right vs 0 = left
    if direction == 1:
        WINDOW.blit(playerR, (playerX, HEIGHT - PLAYER_HEIGHT))
    else:
        WINDOW.blit(playerL, (playerX, HEIGHT - PLAYER_HEIGHT))

    # Draw the lives
    if lives == 3:
        WINDOW.blit(threeLives, (780, 50))
    elif lives == 2:
        WINDOW.blit(twoLives, (780, 50))
    elif lives == 1:
        WINDOW.blit(oneLife, (780, 50))
    else:
        WINDOW.blit(Background, (0, 0))

    pygame.display.update()
