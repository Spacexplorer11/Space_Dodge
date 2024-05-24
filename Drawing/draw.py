import os

import pygame

from Exception_Handling.draw_exception import draw_except

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Fonts
FONT = pygame.font.SysFont("Arial Black", 30)

# Player variables
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 80

try:
    threeLives = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "3_lives.png")), (200, 200))
    twoLives = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "2_lives.png")), (200, 190))
    oneLife = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "1_life.png")), (200, 180))
except FileNotFoundError:
    error = "Lives"
    running = False
    welcome = False
    draw_except(error)

try:
    Background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Space_Background.jpg")),
                                        (WIDTH, HEIGHT))
except FileNotFoundError:
    error = "Background"
    welcome = False
    running = False
    draw_except(error)


def draw(playerL, playerR, playerX, bullets, direction, score, highscore, highscoreBreak,
         mute, lives, muteSymbol, unmuteSymbol, timeText):
    WINDOW.blit(Background, (0, 0))

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(WINDOW, "white", bullet)

    scoreText = FONT.render(f"Score: {score}", 1, "white")
    highScoreTextPt1 = FONT.render(f"Your high score", 1, "white")
    highScoreText_was = FONT.render(f" was {highscore}", 1, "white")
    highScoreText_is = FONT.render(f" is {highscore}", 1, "white")

    WINDOW.blit(timeText, (10, 10))
    WINDOW.blit(scoreText, (WIDTH - 250, 10))
    WINDOW.blit(highScoreTextPt1, (250, 10))

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
