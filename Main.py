# imports
import os
import random
import time

import pygame
from playsound3 import playsound

from Drawing.draw import Background
from Drawing.draw import draw
from Exception_Handling.draw_exception import draw_except
from File_Handling.Loading import load_highscore
from File_Handling.Saving import save_object
from Pause_Menu.pause_function import pause_menu
from Title_screen.draw_title_screen import draw_title
from Tutorial_and_Information.Information import info_screen

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


def main():
    global mute
    running = True  # Keeps the while loop running
    start = False  # Doesn't start the game yet
    highscoreBreak = False  # Tells if the current score is bigger than the highscore
    welcome = True  # Shows the welcome screen or not
    mute = False  # Is the game muted or not
    lives = 3  # Self-explanatory
    highscoreSoundPlayed = False  # Has the highscore sound been played?
    symbolChanged = True  # Has the mute symbol been changed?
    pausedTimes = []  # All the pause time
    totalPausedTime = 0.0  # The total pause time

    # Load all the files/variables
    try:
        title_screen_image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Title_screen.jpg")),
                                                    (WIDTH, HEIGHT))
    except FileNotFoundError:
        welcome = False
        running = False
        error = "Background"
        draw_except(error)

    try:
        playerR = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Player copy.png"), "PlayerR"),
                                         (PLAYER_WIDTH, PLAYER_HEIGHT))
        playerL = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Player.png"), "PlayerL"),
                                         (PLAYER_WIDTH, PLAYER_HEIGHT))
        player = playerL.get_rect()
    except FileNotFoundError:
        welcome = False
        running = False
        error = "Player"
        draw_except(error)

    try:
        muteSymbol = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Mute.png")), (70, 50))
        unmuteSymbol = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Unmute.png")), (70, 50))

        mutePauseSymbol = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Mute.png")), (120, 80))
        unmutePauseSymbol = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Unmute.png")),
                                                   (120, 80))

        pauseSymbol = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Pause_rectangle.png")), (50, 30))
    except FileNotFoundError:
        error = "Symbol"
        welcome = False
        running = False
        draw_except(error)

    sadSoundCheck = os.path.exists(os.path.join("Sounds", "Game_over", "sad-trombone.wav"))
    GameOverSoundCheck = os.path.exists(os.path.join("Sounds", "Game_over", "game-over-sound.wav"))
    highscoreSoundCheck = os.path.exists(os.path.join("Sounds", "Highscore", "highscore.wav"))
    if not (sadSoundCheck or GameOverSoundCheck or highscoreSoundCheck):
        print(sadSoundCheck)
        print(GameOverSoundCheck)
        print(highscoreSoundCheck)
        error = "Sound Effects"
        welcome = False
        running = False
        draw_except(error)
    else:
        sadSound = os.path.join("Sounds", "Game_over", "sad-trombone.wav")
        GameOverSound = os.path.join("Sounds", "Game_over", "game-over-sound.wav")
        highscoreSound = os.path.join("Sounds", "Highscore", "highscore.wav")

    try:
        background_music = pygame.mixer.Sound(os.path.join("Sounds", "Background_music", "background_music.wav"))
        pause_music = pygame.mixer.Sound(os.path.join("Sounds", "Pause_screen", "pause_music.wav"))
    except FileNotFoundError:
        error = "Music"
        welcome = False
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

    direction = 0  # The direction the player is facing( written in binary ) 0 = left, 1 = right

    # Load the high score from file
    highscore = load_highscore(os.path.join("File_Handling", "highscore.pickle"))

    # Play the background music
    pygame.mixer.Sound.set_volume(background_music, 20)
    pygame.mixer.Sound.play(background_music, -1)

    # Draw the welcome screen
    if welcome:
        while not start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    while not start:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                break
                            if event.type == pygame.KEYDOWN:
                                start = True
                                startTime = time.time()
                                break
                        info_screen()
            draw_title(title_screen_image)

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

        # The player's x position reassignment to the local variable
        player.x = playerX

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
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
                    if not mute:
                        mute = True
                    else:
                        mute = False
                if ((muteRect.collidepoint(pygame.mouse.get_pos()) or unmuteRect.collidepoint(pygame.mouse.get_pos()))
                        and mouseclick):
                    if not mute and symbolChanged:
                        mute = True
                    elif symbolChanged:
                        mute = False
                    symbolChanged = False
                if (pauseSymbolRect.collidepoint(pygame.mouse.get_pos()) and mouseclick) or (keys[pygame.K_p]
                                                                                             or keys[pygame.K_ESCAPE]):
                    pauseStartTime = time.time()
                    pause = True
                    if not mute:
                        pygame.mixer.Sound.stop(background_music)
                        pygame.mixer.Sound.play(pause_music, -1)
                    mutePauseRect = mutePauseSymbol.get_rect(x=180, y=430)
                    unmutePauseRect = unmutePauseSymbol.get_rect(x=180, y=430)
                    while pause:
                        pausedTime = time.time() - pauseStartTime
                        playing = pygame.mixer.Sound.get_num_channels(pause_music)
                        if playing == 0 and not mute:
                            pygame.mixer.Sound.play(pause_music)
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
                                        pygame.mixer.Sound.stop(pause_music)
                                    else:
                                        pygame.mixer.Sound.play(pause_music)
                                        mute = False
                                elif keys[pygame.K_p] or keys[pygame.K_ESCAPE]:
                                    pause = False
                                    totalPausedTime = 0.0
                                    pausedTimes.append(round(pausedTime))
                                    pygame.mixer.Sound.stop(pause_music)
                                    for num in pausedTimes:
                                        totalPausedTime += num
                                    break
                                elif mutePauseRect.collidepoint(pygame.mouse.get_pos()) or unmutePauseRect.collidepoint(
                                        pygame.mouse.get_pos()):
                                    if not mute and symbolChanged:
                                        pygame.mixer.Sound.stop(pause_music)
                                        mute = True
                                    elif symbolChanged:
                                        pygame.mixer.Sound.play(pause_music)
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
                        info_screen()

        score += 1
        if score > highscore:
            highscore = score
            highscoreBreak = True
            if not highscoreSoundPlayed:
                highscoreBrokenText = FONT_BIG.render(f"You broke your previous highscore of {score - 1}!", 1, "green")
                WINDOW.blit(highscoreBrokenText, (
                    WIDTH / 2 - highscoreBrokenText.get_width() / 2, HEIGHT / 2 - highscoreBrokenText.get_height() / 2))
                pygame.display.update()
                playsound(highscoreSound)
                highscoreSoundPlayed = True
                pygame.time.delay(1000)

        if bulletCount > bulletAddIncrement:
            for _ in range(3):
                bullet_x = random.randint(0, WIDTH)
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
            if bullet.y > 790:
                bullets.remove(bullet)
            elif bullet.y + bullet.height >= player.y and bullet.colliderect(player):
                bullets.clear()
                lives -= 1
                if lives > 1:
                    WINDOW.blit(Background, (0, 0))
                    pygame.draw.rect(WINDOW, "red", bullet)
                    WINDOW.blit(lostLivesText,
                                (50, HEIGHT / 2 - lostLivesText.get_height()))
                    pygame.display.update()
                    pygame.time.delay(1000)
                elif lives == 1:
                    WINDOW.blit(Background, (0, 0))
                    pygame.draw.rect(WINDOW, "red", bullet)
                    WINDOW.blit(lostLifeText,
                                (50, HEIGHT / 2 - lostLifeText.get_height() / 2))
                    pygame.display.update()
                    pygame.time.delay(1000)
                else:
                    WINDOW.blit(Background, (0, 0))
                    pygame.draw.rect(WINDOW, "red", bullet)
                    pygame.display.update()
                    if highscore >= score:
                        save_object(highscore)
                    pygame.mixer.Sound.fadeout(background_music, 500)
                    WINDOW.blit(Background, (0, 0))
                    loseText = FONT_BIG.render("GAME OVER!", 1, "red")
                    highscoreText = FONT_MEDIUM.render(f"Your score was {score}.", 1, "white")
                    timeText = FONT_MEDIUM.render(f"You played for {round(elapsedTime)} seconds.", 1, "white")
                    WINDOW.blit(loseText,
                                (WIDTH / 2 - loseText.get_width() / 2, HEIGHT / 2 - loseText.get_height() / 2))
                    WINDOW.blit(highscoreText, (WIDTH / 2 - highscoreText.get_width() / 2,
                                                HEIGHT / 2 - loseText.get_height() - highscoreText.get_height() - 100 / 2))
                    WINDOW.blit(timeText, (
                        WIDTH / 2 - timeText.get_width() / 2,
                        HEIGHT / 2 + loseText.get_height() + timeText.get_height() + 100 / 2))
                    pygame.display.update()
                    playsound(GameOverSound)
                    playsound(sadSound)
                    pygame.time.delay(5000)
                    main()
                    break
        if mute:
            pygame.mixer.Sound.stop(background_music)
        elif not mute:
            playing = pygame.mixer.Sound.get_num_channels(background_music)
            if playing == 0:
                pygame.mixer.Sound.play(background_music)

        draw(playerL, playerR, playerX, bullets, direction, highscore, highscoreBreak, mute, lives, muteSymbol,
             unmuteSymbol, timeText, scoreText)

    pygame.quit()


if __name__ == "__main__":
    main()
