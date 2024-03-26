# imports
import random
import time

import pygame

import simpleaudio as sa

from Drawing.draw import draw
from Exception_Handling.draw_exception import draw_except
from File_Handling.Loading import load_highscore
from File_Handling.Saving import save_object
from Sounds.Game_over.Game_over_sound_function import game_over_sound
from Sounds.Highscore.Highscore_sound_function import highscore_sound
from Welcome.Welcome_text_function import welcome_text

pygame.mixer.init()
pygame.font.init()

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Space Dodge")

# All the fonts
FONT = pygame.font.SysFont("Arial Black", 30)
FONT_SMALL = pygame.font.SysFont("Cochin", 30)
FONT_ERROR = pygame.font.SysFont("Phosphate", 50)
FONT_BIG = pygame.font.SysFont("Arial Black", 100)
FONT_MEDIUM = pygame.font.SysFont("Arial Black", 50)

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
    lives = 3
    highscoreSoundPlayed = False

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
        running = False
        error = "Player"
        draw_except(error)

    try:
        threeLives = pygame.transform.scale(pygame.image.load("Assets/3_lives.png"), (200, 200))
        twoLives = pygame.transform.scale(pygame.image.load("Assets/2_lives.png"), (200, 175))
        oneLife = pygame.transform.scale(pygame.image.load("Assets/1_life.png"), (200, 150))
    except FileNotFoundError:
        error = "Lives"
        running = False
        welcome = False
        draw_except(error)

    try:
        muteSymbol = pygame.transform.scale(pygame.image.load("Assets/mute.png"), (70, 50))
        unmuteSymbol = pygame.transform.scale(pygame.image.load("Assets/unmute.png"), (70, 50))
    except FileNotFoundError:
        error = "Mute/unmute symbol"
        welcome = False
        running = False
        draw_except(error)

    try:
        sadSound = sa.WaveObject.from_wave_file("Sounds/Game_over/sad-trombone.wav")
        GameOverSound = sa.WaveObject.from_wave_file("Sounds/Game_over/game-over-sound.wav")
        highscoreSound = sa.WaveObject.from_wave_file("Sounds/Highscore/highscore.wav")
    except FileNotFoundError:
        error = "Sound Effects"
        welcome = False
        running = False
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

    try:
        background_music = pygame.mixer.Sound("Sounds/Background_music/background_music.wav")
    except FileNotFoundError:
        error = "Background Music"
        welcome = False
        running = False
        draw_except(error)

    pygame.mixer.Sound.play(background_music, -1)

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

        score += 1
        if score > highscore:
            highscore = score
            highscoreBreak = True
            if not highscoreSoundPlayed:
                highscoreBrokenText = FONT.render(f"You broke your previous highscore of {score - 1}!", 1, "green")
                WINDOW.blit(highscoreBrokenText, (
                    WIDTH / 2 - highscoreBrokenText.get_width() / 2, HEIGHT / 2 - highscoreBrokenText.get_height() / 2))
                pygame.display.update()
                highscore_sound(mute, highscoreSound)
                highscoreSoundPlayed = True
                pygame.time.delay(1000)
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
            while not start:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        start = True
                        startTime = time.time()
                        break
                welcome_text()

        if mute:
            pygame.mixer.music.pause()
        elif not mute:
            pygame.mixer.music.unpause()

        for bullet in bullets[:]:
            bullet.y += BULLET_VELOCITY
            if bullet.y > 790:
                bullets.remove(bullet)
            elif bullet.y + bullet.height >= player.y and bullet.colliderect(player):
                bullets.clear()
                lives -= 1
                if not (lives <= 1):
                    lostLifeText = FONT.render(f"You lost a life, you are now on {lives} lives!", 1, "red")
                    WINDOW.blit(lostLifeText,
                                (WIDTH / 2 - lostLifeText.get_width() / 2, HEIGHT / 2 - lostLifeText.get_height()))
                    pygame.display.update()
                    pygame.time.delay(1000)
                elif lives == 1:
                    lostLifeText = FONT.render("You lost a life, you are now on 1 life!", 1, "red")
                    WINDOW.blit(lostLifeText,
                                (WIDTH / 2 - lostLifeText.get_width() / 2, HEIGHT / 2 - lostLifeText.get_height() / 2))
                    pygame.display.update()
                    pygame.time.delay(1000)
                else:
                    pygame.draw.rect(WINDOW, "red", bullet)
                    draw(playerL, playerR, playerX, elapsedTime, bullets, direction, score, highscore, highscoreBreak,
                         Background, mute, lives, muteSymbol, unmuteSymbol, threeLives, twoLives, oneLife)
                    hit = True
                    break

        if mute or hit:
            pygame.mixer.Sound.stop(background_music)
        elif not mute:
            playing = pygame.mixer.Sound.get_num_channels(background_music)
            if playing == 0:
                pygame.mixer.Sound.play(background_music)

        if hit:
            highscores.append(score)
            save_object(highscores)
            loseText = FONT_BIG.render("GAME OVER!", 1, "red")
            highscoreText = FONT_MEDIUM.render(f"Your score was {score}.", 1, "white")
            timeText = FONT_MEDIUM.render(f"You played for {round(elapsedTime)} seconds.", 1, "white")
            WINDOW.blit(loseText, (WIDTH / 2 - loseText.get_width() / 2, HEIGHT / 2 - loseText.get_height() / 2))
            WINDOW.blit(highscoreText, (WIDTH / 2 - highscoreText.get_width() / 2,
                                        HEIGHT / 2 - loseText.get_height() - highscoreText.get_height() - 100 / 2))
            WINDOW.blit(timeText, (
                WIDTH / 2 - timeText.get_width() / 2,
                HEIGHT / 2 + loseText.get_height() + timeText.get_height() + 100 / 2))
            pygame.display.update()
            game_over_sound(mute, sadSound, GameOverSound)
            pygame.time.delay(4000)
            break

        draw(playerL, playerR, playerX, elapsedTime, bullets, direction, score, highscore, highscoreBreak,
             Background, mute, lives, muteSymbol, unmuteSymbol, threeLives, twoLives, oneLife)
    pygame.quit()


if __name__ == "__main__":
    main()
