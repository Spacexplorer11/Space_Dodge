import pygame

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Fonts
FONT = pygame.font.SysFont("Arial Black", 30)
FONT_SMALL = pygame.font.SysFont("Cochin", 30)
FONT_ERROR = pygame.font.SysFont("Phosphate", 50)

# Player variables
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 80
PLAYER_VELOCITY = 5


def draw(playerL, playerR, playerX, elapsedTime, bullets, direction, score, highscore, highscoreBreak, Background, mute):
    WINDOW.blit(Background, (0, 0))

    timeText = FONT.render(f"Time: {round(elapsedTime)}s", 1, "white")
    scoreText = FONT.render(f"Score: {score}", 1, "white")
    highScoreTextPt1 = FONT.render(f"Your high score", 1, "white")
    highScoreText_was = FONT.render(f" was {highscore}", 1, "white")
    highScoreText_is = FONT.render(f" is {highscore}", 1, "white")
    muteSymbol = pygame.transform.scale(pygame.image.load("Assets/mute.png"), (70, 50))
    unmuteSymbol = pygame.transform.scale(pygame.image.load("Assets/unmute.png"), (70, 50))

    WINDOW.blit(timeText, (10, 10))
    WINDOW.blit(scoreText, (WIDTH - 250, 10))

    if mute:
        WINDOW.blit(muteSymbol,(timeText.get_width() + 10, 10))
    else:
        WINDOW.blit(unmuteSymbol,(timeText.get_width() + 10, 10))

    if highscoreBreak:
        WINDOW.blit(highScoreTextPt1, (250, 10))
        WINDOW.blit(highScoreText_is, (500, 10))
    else:
        WINDOW.blit(highScoreTextPt1, (250, 10))
        WINDOW.blit(highScoreText_was, (500, 10))

    # 1 = right vs 0 = left
    if direction == 1:
        WINDOW.blit(playerR, (playerX, HEIGHT - PLAYER_HEIGHT))
    else:
        WINDOW.blit(playerL, (playerX, HEIGHT - PLAYER_HEIGHT))

    for bullet in bullets:
        pygame.draw.rect(WINDOW, "white", bullet)

    pygame.display.update()
