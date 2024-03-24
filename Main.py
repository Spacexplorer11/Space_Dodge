# imports
import random
import time
import pygame

from Drawing.draw import draw
from Exception_Handling.draw_exception import draw_except
from File_Handling.Loading import load_highscore
from File_Handling.Saving import save_object
from Sound_effects.Game_over.Game_over_sound_function import game_over_sound
from Sound_effects.Highscore.Highscore_sound_function import highscore_sound

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

FONT = pygame.font.SysFont("Arial Black", 30)
FONT_SMALL = pygame.font.SysFont("Cochin", 30)
FONT_ERROR = pygame.font.SysFont("Phosphate", 50)

# Player variables
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 80
PLAYER_VELOCITY = 5

# Bullet variables
BULLET_WIDTH = 10
BULLET_HEIGHT = 20
BULLET_VELOCITY = 3


def main():
    running = True
    start = False
    highscoreBreak = False
    welcome = True
    mute = False

    try:
        Background = pygame.transform.scale(pygame.image.load("Assets/Space_Background.jpg"), (WIDTH, HEIGHT))
    except FileNotFoundError:
        error = "Background"
        welcome = False
        running = False
        draw_except(error)

    try:
        playerR = pygame.transform.scale(pygame.image.load("Assets/Player copy.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
        playerL = pygame.transform.scale(pygame.image.load("Assets/Player.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
        player = playerL.get_rect()
    except FileNotFoundError:
        welcome = False
        error = "Player"
        draw_except(error)

    clock = pygame.time.Clock()

    startTime = time.time()

    score = 0

    bulletAddIncrement = 2000
    bulletCount = 0  # Tells us when to add the bullet

    bullets = []

    playerX = 500
    player.x = playerX
    player.y = HEIGHT - PLAYER_HEIGHT

    direction = 0

    hit = False

    # Load the high score from file as a list
    highscores = load_highscore("File_Handling/highscore.pickle")

    # If highscores is not a list add 0 to make a list
    if not highscores.__class__ == list:
        highscores = [highscores, 0]

    if len(highscores) >= 2:
        # Finds the highest score
        highscore1 = sorted(highscores, reverse=True)
        highscore = highscore1[0]

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_m]:
                    if not mute:
                        mute = True
                    else:
                        mute = False

        score = score + 1
        if score > highscore:
            highscore = score
            highscoreBreak = True
            highscore_sound(mute)
        bulletCount += clock.tick(60)
        elapsedTime = time.time() - startTime
        player.x = playerX

        if bulletCount > bulletAddIncrement:
            for _ in range(3):
                bullet_x = random.randint(0, WIDTH - BULLET_WIDTH)
                bullet = pygame.Rect(bullet_x, -BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT)
                bullets.append(bullet)

            bulletAddIncrement = max(400, bulletAddIncrement - 50)
            bulletCount = 0


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:
            direction = 0
            playerX -= PLAYER_VELOCITY
            player.x = playerX
        if keys[pygame.K_d] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            direction = 1
            playerX += PLAYER_VELOCITY
            player.x = playerX

        if welcome:
            welcomeText1 = FONT.render("Welcome to Space Dodge!", 1, "white")
            welcomeText2 = FONT.render("Use A & D keys to move left and right!", 1, "white")
            welcomeText3 = FONT.render("Try not to hit the bullets!", 1, "white")
            startText = FONT_SMALL.render("Click any key to continue!", 1, "white")
            muteInstructionText = FONT.render("Click M to mute and unmute!", 1, "white")
            welcomeText1Place = WIDTH / 2 - welcomeText1.get_width() / 2, HEIGHT / 2 - welcomeText1.get_height() / 2
            WINDOW.blit(welcomeText1, welcomeText1Place)
            WINDOW.blit(welcomeText2, (WIDTH / 2 - welcomeText2.get_width() / 2,
                                       HEIGHT / 2 - (welcomeText1.get_height() - welcomeText2.get_height() - 30) / 2))
            WINDOW.blit(welcomeText3, (WIDTH / 2 - welcomeText3.get_width() / 2,
                                       HEIGHT / 2 - (
                                               welcomeText1.get_height() - welcomeText2.get_height() - welcomeText3.
                                               get_height() - 60) / 2))
            WINDOW.blit(muteInstructionText, (WIDTH / 2 - muteInstructionText.get_width() / 2,
                                              HEIGHT / 2 - (
                                                      welcomeText1.get_height() - welcomeText2.get_height() - welcomeText3.
                                                      get_height() - muteInstructionText.get_height() - 90) / 2))
            WINDOW.blit(startText, (WIDTH / 2 - startText.get_width() / 2, 740))
            pygame.display.update()
            while not start:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        start = True
                        break
                    elif event.type == pygame.KEYDOWN:
                        start = True
                        break
            startTime = time.time()
            welcome = False

        for bullet in bullets[:]:
            bullet.y += BULLET_VELOCITY
            if bullet.y > 790:
                bullets.remove(bullet)
            elif bullet.y + bullet.height >= player.y and bullet.colliderect(player):
                pygame.draw.rect(WINDOW, "red", bullet)
                hit = True
                break

        if hit:
            highscores.append(score)
            save_object(highscores)
            loseText = FONT.render("GAME OVER!", 1, "red")
            WINDOW.blit(loseText, (WIDTH / 2 - loseText.get_width() / 2, HEIGHT / 2 - loseText.get_height() / 2))
            pygame.display.update()
            game_over_sound(mute)
            bullets.clear()
            pygame.time.delay(4000)
            break

        draw(playerL, playerR, playerX, elapsedTime, bullets, direction, score, highscore, highscoreBreak, Background, mute)
    pygame.quit()


if __name__ == "__main__":
    main()
