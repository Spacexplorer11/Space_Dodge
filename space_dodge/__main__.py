# imports
import os
import random
import time
import logging
from logging import getLogger


import pygame

from drawing.draw import Background
from drawing.draw import draw
from drawing.exception_handling.draw_exception import draw_except
from file_handling.loading import load_highscore
from file_handling.saving import save_object
from drawing.pause_menu.pause_function import pause_menu
from drawing.title_screen.draw_title_screen import draw_title
from drawing.tutorial_and_information.keybindings import keybindings_screen
from drawing.tutorial_and_information.welcome import welcome_screen
from file_handling.utility import ref

pygame.mixer.init()
pygame.font.init()
pygame.init()

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
FONT_MEDIUM = pygame.font.SysFont("Arial Black", 45)

# Player variables
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 80
PLAYER_VELOCITY = 5

# Bullet variables
BULLET_WIDTH = 10
BULLET_HEIGHT = 20
BULLET_VELOCITY = 3

logfile = ref('mylog.log')
logging.basicConfig(filename=logfile, level=logging.INFO)
logger = getLogger(__name__)


# Create a simple surface for the bullet (white rectangle)
bullet_surface = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
bullet_surface.fill((255, 255, 255))
bullet_mask = pygame.mask.from_surface(bullet_surface)


def main():
    global mute
    running = True  # Keeps the while loop running
    start = False  # Doesn't start the game yet
    highscoreBreak = False  # Tells if the current score is bigger than the highscore
    welcome = False  # Shows the welcome screen
    mute = False  # Is the game muted or not
    lives = 3  # Self-explanatory
    highscoreSoundPlayed = False  # Has the highscore sound been played?
    symbolChanged = True  # Has the mute symbol been changed?
    pausedTimes = []  # All the pause time
    totalPausedTime = 0.0  # The total pause time


    # Load all the files/variables
    try:
        playerR = pygame.transform.scale(pygame.image.load(ref("assets/player_r.png"), "PlayerR"),
                                         (PLAYER_WIDTH, PLAYER_HEIGHT))
        playerL = pygame.transform.scale(pygame.image.load(ref("assets/player_l.png"), "PlayerL"),
                                         (PLAYER_WIDTH, PLAYER_HEIGHT))
        player = playerL.get_rect()
    except FileNotFoundError:
        logger.exception('Player not found')  # log the exception in a file
        running = False
        error = "Player"
        draw_except(error)

    try:
        muteSymbol = pygame.transform.scale(pygame.image.load(ref("assets/mute.png")), (70, 50))
        unmuteSymbol = pygame.transform.scale(pygame.image.load(ref("assets/unmute.png")), (70, 50))

        mutePauseSymbol = pygame.transform.scale(pygame.image.load(ref("assets/mute.png")), (120, 80))
        unmutePauseSymbol = pygame.transform.scale(pygame.image.load(ref("assets/unmute.png")),
                                                   (120, 80))

        pauseSymbol = pygame.transform.scale(pygame.image.load(ref("assets/pause_rectangle.png")), (50, 30))
    except FileNotFoundError:
        logger.exception('Mute or Unmute or Pause Symbol not found')  # log the exception in a file
        error = "Symbol"
        running = False
        draw_except(error)

    try:
        sadSound = pygame.mixer.Sound(ref("sounds/game_over/sad-trombone.mp3"))
        GameOverSound = pygame.mixer.Sound(ref("sounds/game_over/game-over-sound.mp3"))
        highscoreSound = pygame.mixer.Sound(ref("sounds/highscore/highscore.mp3"))
    except FileNotFoundError:
        logger.exception('Sound not found')  # log the exception in a file
        error = "Sound Effects"
        running = False
        draw_except(error)

    background_music_check = os.path.exists(ref("sounds/background_music/background_music.mp3"))
    pause_music_check = os.path.exists(ref("sounds/pause_screen/pause_music.mp3"))
    if not (background_music_check or pause_music_check):
        logger.exception('Music not found')  # log the exception in a file
        error = "Music"
        running = False
        draw_except(error)

    clock = pygame.time.Clock()  # The clock for the game

    startTime = time.time()  # The time the game started

    score = 0  # The score of the player

    bulletAddIncrement = 2000  # The time between adding bullets
    bulletCount = 0  # Tells us when to add the bullet

    bullets = []  # The list of bullets

    playerX = 500  # The x position of the player
    player.x = playerX  # The x position of the player assigned to local variable
    player.y = HEIGHT - PLAYER_HEIGHT  # The y position of the player
    playerY = player.y  # The y position of the player assigned to local variable

    direction = 0  # The direction the player is facing( written in binary ) 0 = left, 1 = right

    # Load the high score from file
    highscore = load_highscore(ref("file_handling/highscore.pickle"))

    # Play the background music
    pygame.mixer.music.load(ref("sounds/background_music/background_music.mp3"))
    pygame.mixer.music.set_volume(20)
    pygame.mixer.music.play(-1)

    # Draw the title screen
    if not start:
        welcome = draw_title(start, welcome)

    while welcome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                welcome = False
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                while welcome:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            welcome = False
                            running = False
                            break
                        if event.type == pygame.KEYDOWN:
                            welcome = False
                            startTime = time.time()
                            break
                    keybindings_screen()
        welcome_screen()

    # The text for when the player loses a life
    lostLivesText = FONT_MEDIUM.render("You lost a life, you are now on 2 lives!", 1, "red")
    lostLifeText = FONT_MEDIUM.render("You lost a life, you are now on 1 life!", 1, "red")

    # The main game loop
    while running:

        # The time the game was paused & playing
        elapsedTime = time.time() - startTime
        elapsedTime -= totalPausedTime

        # Get the keys pressed
        keys = pygame.key.get_pressed()

        # The text for the time and score( it's updated every frame )
        timeText = FONT.render(f"Time: {round(elapsedTime)}", 1, "white")
        scoreText = FONT.render(f"Score: {score}", 1, "white")

        # The rectangles for the symbols( it's updated every frame )
        muteRect = muteSymbol.get_rect(x=(timeText.get_width() + 10), y=10)
        unmuteRect = unmuteSymbol.get_rect(x=(timeText.get_width() + 10), y=10)
        pauseSymbolRect = pauseSymbol.get_rect(x=(scoreText.get_width() + 745), y=19)

        # The framerate of the game
        bulletCount += clock.tick(60)

        player_mask = pygame.mask.from_surface(playerL if direction == 0 else playerR)

        # The player's x position reassignment to the local variable
        player.x = playerX

        # Event handling
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                running = False
                break
            # Check if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONUP:
                symbolChanged = True
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                mouseclick = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseclick = True
                if keys[pygame.K_a] or keys[pygame.K_d]:
                    pass
                    break
                if keys[pygame.K_m]:
                    mute = True if not mute else False
                if ((muteRect.collidepoint(pygame.mouse.get_pos()) or unmuteRect.collidepoint(pygame.mouse.get_pos()))
                        and mouseclick):
                    mute = True if not mute and symbolChanged else False
                    symbolChanged = False
                if (pauseSymbolRect.collidepoint(pygame.mouse.get_pos()) and mouseclick) or (keys[pygame.K_p]
                                                                                             or keys[pygame.K_ESCAPE]):
                    pauseStartTime = time.time()
                    pause = True
                    pygame.mixer.music.load(
                        ref("sounds/background_music/pause_screen/pause_music.mp3"))
                    if not mute:
                        pygame.mixer.music.play(-1)
                    mutePauseRect = mutePauseSymbol.get_rect(x=180, y=430)
                    unmutePauseRect = unmutePauseSymbol.get_rect(x=180, y=430)
                    while pause:
                        pausedTime = time.time() - pauseStartTime
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pause = False
                                running = False
                                break
                            if event.type == pygame.MOUSEBUTTONUP:
                                symbolChanged = True
                            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_m]:
                                    if not mute:
                                        mute = True
                                        pygame.mixer.music.pause()
                                    else:
                                        pygame.mixer.music.unpause()
                                        mute = False
                                elif keys[pygame.K_p] or keys[pygame.K_ESCAPE]:
                                    pause = False
                                    totalPausedTime = 0.0
                                    pausedTimes.append(round(pausedTime))
                                    pygame.mixer.music.stop()
                                    pygame.mixer.music.unload()
                                    pygame.mixer.music.load(
                                        ref("sounds/background_music/background_music.mp3"))
                                    pygame.mixer.music.play(-1)
                                    for num in pausedTimes:
                                        totalPausedTime += num
                                    break
                                elif mutePauseRect.collidepoint(pygame.mouse.get_pos()) or unmutePauseRect.collidepoint(
                                        pygame.mouse.get_pos()):
                                    if not mute and symbolChanged:
                                        pygame.mixer.music.pause()
                                        mute = True
                                    elif symbolChanged:
                                        pygame.mixer.music.unpause()
                                        mute = False
                                    symbolChanged = False
                        pause_menu(score, elapsedTime, highscore, highscoreBreak, mute)
                if keys[pygame.K_k] or keys[pygame.K_i]:
                    info_screen_active = True
                    pauseStartTime = time.time()
                    keyPress = True
                    while info_screen_active:
                        pausedTime = time.time() - pauseStartTime
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP:
                                keyPress = False
                            if event.type == pygame.QUIT:
                                running = False
                                info_screen_active = False
                                break
                            if event.type == pygame.KEYDOWN and not keyPress:
                                keyPress = True
                                totalPausedTime = 0.0
                                pausedTimes.append(round(pausedTime))
                                info_screen_active = False
                                for num in pausedTimes:
                                    totalPausedTime += num
                                break
                        keybindings_screen()

        score += 1
        if score > highscore:
            highscore = score
            if highscore > 1:
                highscoreBreak = True
            if not highscoreSoundPlayed:
                highscoreBrokenText = FONT_MEDIUM.render(f"You broke your previous highscore of {score - 1}!", 1,
                                                         "green")
                WINDOW.blit(highscoreBrokenText, (
                    WIDTH / 2 - highscoreBrokenText.get_width() / 2, HEIGHT / 2 - highscoreBrokenText.get_height() / 2))
                pygame.display.update()
                pygame.mixer.Sound.play(highscoreSound)
                highscoreSoundPlayed = True
                pygame.time.delay(1000)

        if bulletCount > bulletAddIncrement:
            for _ in range(3):
                bullet_x = random.randint(0 + BULLET_WIDTH, WIDTH - BULLET_WIDTH)
                bullet = pygame.Rect(bullet_x, -BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT)
                bullets.append(bullet)

            bulletAddIncrement = max(400, bulletAddIncrement - 50)
            bulletCount = 0

        if keys[pygame.K_a] and playerX - PLAYER_VELOCITY >= 0:
            direction = 0
            playerX -= PLAYER_VELOCITY
        if keys[pygame.K_d] and playerX + PLAYER_VELOCITY + player.width <= WIDTH:
            direction = 1
            playerX += PLAYER_VELOCITY

        for bullet in bullets[:]:
            bullet.y += BULLET_VELOCITY
            if bullet.y > HEIGHT - BULLET_HEIGHT:
                bullets.remove(bullet)
            else:
                bullet_rect = pygame.Rect(bullet.x, bullet.y, BULLET_WIDTH, BULLET_HEIGHT)
                offset = (bullet_rect.x - player.x, bullet_rect.y - player.y)
                if player_mask.overlap(bullet_mask, offset):
                    bullets.clear()
                    lives -= 1
                    if lives > 1:
                        WINDOW.blit(Background, (0, 0))
                        pygame.draw.rect(WINDOW, "red", bullet)
                        WINDOW.blit(lostLivesText, (50, HEIGHT / 2 - lostLivesText.get_height()))
                        pygame.display.update()
                        pygame.time.delay(1000)
                    elif lives == 1:
                        WINDOW.blit(Background, (0, 0))
                        pygame.draw.rect(WINDOW, "red", bullet)
                        WINDOW.blit(lostLifeText, (50, HEIGHT / 2 - lostLifeText.get_height() / 2))
                        pygame.display.update()
                        pygame.time.delay(1000)
                    else:
                        WINDOW.blit(Background, (0, 0))
                        pygame.draw.rect(WINDOW, "red", bullet)
                        pygame.display.update()
                        if highscore >= score:
                            save_object(highscore)
                        pygame.mixer.music.fadeout(1000)
                        WINDOW.blit(Background, (0, 0))
                        loseText = FONT_BIG.render("GAME OVER!", 1, "red")
                        highscoreText = FONT_MEDIUM.render(f"Your score was {score}.", 1, "white")
                        timeText = FONT_MEDIUM.render(f"You played for {round(elapsedTime)} seconds.", 1, "white")
                        WINDOW.blit(loseText,
                                    (WIDTH / 2 - loseText.get_width() / 2, HEIGHT / 2 - loseText.get_height() / 2))
                        WINDOW.blit(highscoreText, (WIDTH / 2 - highscoreText.get_width() / 2,
                                                    HEIGHT / 2 - loseText.get_height() - highscoreText.get_height() - 100 / 2))
                        WINDOW.blit(timeText, (WIDTH / 2 - timeText.get_width() / 2,
                                               HEIGHT / 2 + loseText.get_height() + timeText.get_height() + 100 / 2))
                        pygame.display.update()
                        pygame.mixer.Sound.play(GameOverSound)
                        pygame.mixer.Sound.play(sadSound)
                        pygame.time.delay(5000)
                        start = False
                        main()
                        break
        if mute:
            pygame.mixer.music.pause()
        elif not mute:
            pygame.mixer.music.unpause()

        draw(playerL, playerR, playerX, bullets, direction, highscore, highscoreBreak, mute, lives, muteSymbol,
             unmuteSymbol, timeText, scoreText)

    pygame.quit()


if __name__ == "__main__":
    main()
