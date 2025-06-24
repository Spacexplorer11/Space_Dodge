# Imports
import os
import pathlib
import subprocess
import sys
import time
import venv

from file_handling.constants_and_file_loading import logger

# Check if running inside a virtual environment
if sys.prefix == sys.base_prefix:
    venv_path = os.path.join(os.path.dirname(__file__), 'venv')

    # If venv doesn't exist, create it and restart the script
    if not os.path.isdir(venv_path):
        print("🔧 Creating a virtual environment...")
        logger.info(f"Creating a virtual environment at {venv_path}")
        venv.create(venv_path, with_pip=True)
        print("⚙️ Restarting the script inside the virtual environment...")
        logger.info("Restarting the script inside the virtual environment")
        activate_script = os.path.join(venv_path, 'bin', 'python') if sys.platform != 'win32' else os.path.join(
            venv_path, 'Scripts', 'python.exe')
        os.execv(activate_script, [activate_script] + sys.argv)
    else:
        print("⚙️ Re-starting the script inside the virtual environment...")
        logger.info("Re-starting the script inside the virtual environment")
        activate_script = os.path.join(venv_path, 'bin', 'python') if sys.platform != 'win32' else os.path.join(
            venv_path, 'Scripts', 'python.exe')
        os.execv(activate_script, [activate_script] + sys.argv)

# Check if all required packages are installed in the virtual environment
# Construct and validate requirements.txt path more securely
script_dir = os.path.dirname(os.path.abspath(__file__))
requirements_file = os.path.join(script_dir, 'requirements.txt')

# Ensure the file exists and is within the expected directory
req_path = pathlib.Path(requirements_file).resolve()
if req_path.is_file() and script_dir in str(req_path) and req_path.name == "requirements.txt":
    print("📦 Installing all required packages from requirements.txt...")
    logger.info(f"Installing required packages from {requirements_file}")
    # Safe static command with validated file path
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", str(req_path)],
        check=True
    )
else:
    raise FileNotFoundError(
        f"requirements.txt not found in script directory: {script_dir}"
    )

import pygame

# Import the classes' modules
from classes.bullet import Bullet
from classes.button import Button
from classes.player import Player
from drawing.draw import draw
from drawing.pause_menu.pause_function import pause_menu
from drawing.title_screen.draw_title_screen import draw_title
from drawing.tutorial_and_information.keybindings import keybindings_screen
# Import all constant variables
from file_handling.constants_and_file_loading import (FONT,
                                                      FONT_MEDIUM, FONT_BIG, WIDTH, HEIGHT, WINDOW)
# Import all the files( images, sounds, etc. )
from file_handling.constants_and_file_loading import (muteImage, unmuteImage, pauseButtonImage, game_background,
                                                      sadSound, GameOverSound, highscoreSound)
from file_handling.loading_func import load_highscore
from file_handling.saving import save_object
from file_handling.utility import ref

pygame.mixer.init()
pygame.font.init()
pygame.init()


def main():
    highscoreBreak = False  # Tells if the current score is bigger than the highscore
    running = True  # Is the game running or not
    mute = False  # Is the game muted or not
    lives = 4  # Self-explanatory
    highscoreSoundPlayed = False  # Has the highscore sound been played?
    pausedTimes = []  # The total pause time
    startTime = time.time()  # The time the game started (will be overwritten by title screen)
    last_time = time.time()
    explosions = []  # The list of explosions
    player = Player()  # Create the player object
    muteButton = Button(muteImage, 132, 10)  # Create the mute symbol object
    unmuteButton = Button(unmuteImage, 132, 10)  # Create the unmute symbol object
    pauseButton = Button(pauseButtonImage, 900, 10)  # Create the pause symbol object
    firstTime = True  # Is this the first time the game is started?

    clock = pygame.time.Clock()  # The clock for the game

    score = 0  # The score of the player

    bulletAddIncrement = 2000  # The time between adding bullets
    bulletCount = 0  # Tells us when to add the bullet

    bullets = []  # The list of bullets

    # Load the high score from file
    highscore, highscoreFileFound = load_highscore(ref("file_handling/highscore.pickle"))

    # The text for when the player loses a life
    lostLivesText = FONT_MEDIUM.render("You lost a life, you are now on 2 lives!", 1, "red")
    lostLifeText = FONT_MEDIUM.render("You lost a life, you are now on 1 life!", 1, "red")

    # The main game loop
    while running:

        if lives == 4:
            # Draw the title screen
            logger.info("Drawing the title screen")
            running, startTime, mute = draw_title(mute, firstTime)
            lives = 3
            pausedTimes.clear()
            score = 0
            # Load the high score from file
            highscore, highscoreFileFound = load_highscore(ref("file_handling/highscore.pickle"))
            # Play the background music
            pygame.mixer.music.load(ref("assets/sounds/background_music/background_music.mp3"))
            pygame.mixer.music.set_volume(20)
            pygame.mixer.music.play(-1)
            logger.info("Main game loop started")
            continue

        # The time the game was paused & playing
        elapsedTime = time.time() - startTime
        elapsedTime -= sum(pausedTimes)

        # These variables are used to calculate the time between frames for the explosion animation
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        # Get the keys pressed
        keys = pygame.key.get_pressed()

        # The text for the time and score( it's updated every frame )
        timeText = FONT.render(f"Time: {round(elapsedTime)}", 1, "white")
        scoreText = FONT.render(f"Score: {score}", 1, "white")

        # The rectangles for the symbols( it's updated every frame )
        muteButton.update_rect(timeText.get_width() + 10)
        unmuteButton.update_rect(timeText.get_width() + 10)
        pauseButton.update_rect(scoreText.get_width() + 745)

        # The framerate of the game
        bulletCount += clock.tick(60)

        # The mask for the player
        player_mask = pygame.mask.from_surface(player.image)

        # Event handling
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                if score >= highscore:
                    save_object(score)
                running = False
                pygame.mixer.music.stop()
                break
            # Check if the mouse is clicked or a key is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a] or keys[pygame.K_d]:
                    pass
                    break
                if keys[pygame.K_m] or muteButton.clicked() or unmuteButton.clicked():
                    mute = not mute
                if keys[pygame.K_k] or keys[pygame.K_i]:
                    running, pausedTime = keybindings_screen(lives)
                    pausedTimes.append(pausedTime)
                if (pauseButton.clicked() or
                        keys[pygame.K_p]):
                    running, mute, pausedTime = pause_menu(score, elapsedTime, highscore, highscoreBreak, mute)
                    pausedTimes.append(pausedTime)

        if highscore == 0 and not highscoreFileFound:
            highscore = 1

        score += 1
        if score > highscore:
            highscore = score
            highscoreBreak = True

            if highscoreFileFound and not highscoreSoundPlayed:
                highscoreBrokenText = FONT.render(f"You broke your previous highscore of {score - 1}!", 1, "green")
                WINDOW.blit(highscoreBrokenText, (
                    WIDTH / 2 - highscoreBrokenText.get_width() / 2,
                    HEIGHT / 2 - highscoreBrokenText.get_height() / 2))
                pygame.display.update()
                if not mute:
                    pygame.mixer.Sound.play(highscoreSound)
                highscoreSoundPlayed = True
                startTime1 = time.time()
                while not time.time() > startTime1 + 1:  # A while loop which waits for 1 second
                    for event in pygame.event.get():  # but the game can still be quit during this time
                        if event.type == pygame.QUIT:
                            if score >= highscore:
                                save_object(score)
                            running = False
                            break
                    if not running:
                        break

        if bulletCount > bulletAddIncrement:
            for _ in range(3):
                bullet = Bullet()
                bullets.append(bullet)

            bulletAddIncrement = max(400, bulletAddIncrement - 50)
            bulletCount = 0

        if keys[pygame.K_a]:
            player.direction = 0
            player.x -= player.velocity
        if keys[pygame.K_d]:
            player.direction = 1
            player.x += player.velocity

        for bullet in bullets[:]:
            bullet.y += bullet.velocity
            if bullet.y > HEIGHT - bullet.height:
                bullets.remove(bullet)
            else:
                bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
                offset = (bullet_rect.x - player.x, bullet_rect.y - player.y)
                if player_mask.overlap(bullet.mask, offset):
                    bullets.clear()
                    lives -= 1
                    if lives > 0:
                        WINDOW.blit(game_background, (0, 0))
                        WINDOW.blit(lostLivesText if lives > 1 else lostLifeText,
                                    (50, HEIGHT / 2 - lostLivesText.get_height()))
                        pygame.display.update()
                        startTime1 = time.time()
                        while not time.time() > startTime1 + 1:  # A while loop which waits for 1 second
                            for event in pygame.event.get():  # but the game can still be quit during this time
                                if event.type == pygame.QUIT:
                                    if score >= highscore:
                                        save_object(score)
                                    running = False
                                    break
                            if not running:
                                break
                    else:
                        WINDOW.blit(game_background, (0, 0))
                        pygame.display.update()
                        if score >= highscore or highscore == 0:
                            save_object(score)
                        pygame.mixer.music.fadeout(1000)
                        WINDOW.blit(game_background, (0, 0))
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
                        if not mute:
                            pygame.mixer.Sound.play(GameOverSound)
                            pygame.mixer.Sound.play(sadSound)
                        startTime1 = time.time()
                        while not time.time() > startTime1 + 5:  # A while loop which waits for 5 seconds
                            for event in pygame.event.get():  # but the game can still be quit during this time
                                if event.type == pygame.QUIT:
                                    running = False
                                    break
                            if not running:
                                break
                        lives = 4
                        firstTime = False
                        break
            if pygame.mixer.music.get_busy() is False and mute is False:
                pygame.mixer.music.load(ref("assets/sounds/background_music/background_music.mp3"))
                pygame.mixer.music.play(-1)
            pygame.mixer.music.pause() if mute else pygame.mixer.music.unpause()  # Pause or unpause the music

        if not running:
            save_object(score) if score >= highscore else None
            continue

        draw(player, bullets, highscore, highscoreBreak, mute, lives, timeText, scoreText, explosions,
             muteButton, unmuteButton, pauseButton)

    pygame.quit()


if __name__ == "__main__":
    main()
