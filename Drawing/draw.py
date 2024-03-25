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


def draw(playerL, playerR, playerX, elapsedTime, bullets, direction, score, highscore, highscoreBreak, Background,
         mute, lives, muteSymbol, unmuteSymbol, threeLives, twoLives, oneLife):
    WINDOW.blit(Background, (0, 0))

    timeText = FONT.render(f"Time: {round(elapsedTime)}s", 1, "white")
    scoreText = FONT.render(f"Score: {score}", 1, "white")
    highScoreTextPt1 = FONT.render(f"Your high score", 1, "white")
    highScoreText_was = FONT.render(f" was {highscore}", 1, "white")
    highScoreText_is = FONT.render(f" is {highscore}", 1, "white")

    WINDOW.blit(timeText, (10, 10))
    WINDOW.blit(scoreText, (WIDTH - 250, 10))

    # Show the mute/unmute symbol
    if mute:
        WINDOW.blit(muteSymbol, (timeText.get_width() + 10, 10))
    else:
        WINDOW.blit(unmuteSymbol, (timeText.get_width() + 10, 10))

    # Check if the highscore is higher than the current score and if it is then say highscore "is" not "was"
    if highscoreBreak:
        WINDOW.blit(highScoreTextPt1, (250, 10))
        WINDOW.blit(highScoreText_is, (500, 10))
    else:
        WINDOW.blit(highScoreTextPt1, (250, 10))
        WINDOW.blit(highScoreText_was, (500, 10))

    # Changing where the player faces
    # 1 = right vs 0 = left
    if direction == 1:
        WINDOW.blit(playerR, (playerX, HEIGHT - PLAYER_HEIGHT))
    else:
        WINDOW.blit(playerL, (playerX, HEIGHT - PLAYER_HEIGHT))

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(WINDOW, "white", bullet)

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
