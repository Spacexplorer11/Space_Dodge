# imports
import random
import time

import pygame

from space_dodge.drawing.draw import draw
from space_dodge.file_handling.loading_func import load_highscore
from space_dodge.file_handling.saving import save_object
from space_dodge.drawing.pause_menu.pause_function import pause_menu
from space_dodge.drawing.title_screen.draw_title_screen import draw_title
from space_dodge.drawing.tutorial_and_information.keybindings import keybindings_screen
from space_dodge.file_handling.utility import ref

# Import all constant variables & files
from file_handling.constants_and_file_loading import (PLAYER_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT,
                                                      PLAYER_VELOCITY, BULLET_VELOCITY, FONT,
                                                      FONT_MEDIUM, FONT_BIG, WIDTH, HEIGHT, WINDOW)

# Import all the files( images, sounds, etc. )
from file_handling.constants_and_file_loading import (playerL, playerR, muteSymbol, unmuteSymbol, pauseSymbol, background,
                                                      bullet_texture, player, sadSound, GameOverSound, highscoreSound)

pygame.mixer.init()
pygame.font.init()
pygame.init()


def main():
    running = True  # Keeps the while loop running
    highscoreBreak = False  # Tells if the current score is bigger than the highscore
    mute = False  # Is the game muted or not
    lives = 3  # Self-explanatory
    highscoreSoundPlayed = False  # Has the highscore sound been played?
    pausedTimes = []  # All the pause time
    totalPausedTime = 0.0  # The total pause time
    highscore_file_not_found = False  # Is the highscore file not found?
    last_time = time.time()
    explosions = []  # The list of explosions

    # Create a mask for the bullet
    bullet_mask = pygame.mask.from_surface(bullet_texture)

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
    highscore = load_highscore(ref("file_handling/highscore.pickle"))
    if highscore == 0:
        highscore_file_not_found = True

    # Draw the title screen
    draw_title()

    # The text for when the player loses a life
    lostLivesText = FONT_MEDIUM.render("You lost a life, you are now on 2 lives!", 1, "red")
    lostLifeText = FONT_MEDIUM.render("You lost a life, you are now on 1 life!", 1, "red")

    # Play the background music
    pygame.mixer.music.load(ref("sounds/background_music/background_music.mp3"))
    pygame.mixer.music.set_volume(20)
    pygame.mixer.music.play(-1)

    # The main game loop
    while running:

        # The time the game was paused & playing
        elapsedTime = time.time() - startTime
        elapsedTime -= totalPausedTime
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

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

        # The mask for the player
        player_mask = pygame.mask.from_surface(playerL if direction == 0 else playerR)

        # The player's x position reassignment to the local variable
        player.x = playerX

        # Event handling
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                if highscore >= score:
                    save_object(highscore)
                running = False
                break
            # Check if the mouse is clicked or a key is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a] or keys[pygame.K_d]:
                    pass
                    break
                if keys[pygame.K_m]:
                    mute = not mute
                if keys[pygame.K_k] or keys[pygame.K_i]:
                    keybindings_screen(pausedTimes)
                if ((muteRect.collidepoint(pygame.mouse.get_pos()) or unmuteRect.collidepoint(pygame.mouse.get_pos()))
                        and event.type == pygame.MOUSEBUTTONDOWN):
                    mute = not mute
                if (pauseSymbolRect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN) or (
                        keys[pygame.K_p]
                        or keys[pygame.K_ESCAPE]):
                    running, pause, totalPausedTime = pause_menu(score, elapsedTime, highscore, highscoreBreak, mute, pausedTimes)
                    break


        score += 1
        if score > highscore:
            highscore = score
            highscoreBreak = True
            if not highscoreSoundPlayed and not highscore_file_not_found:
                highscoreBrokenText = FONT.render(f"You broke your previous highscore of {score - 1}!", 1,
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
                        WINDOW.blit(background, (0, 0))
                        WINDOW.blit(lostLivesText, (50, HEIGHT / 2 - lostLivesText.get_height()))
                        pygame.display.update()
                        pygame.time.delay(1000)
                    elif lives == 1:
                        WINDOW.blit(background, (0, 0))
                        WINDOW.blit(lostLifeText, (50, HEIGHT / 2 - lostLifeText.get_height() / 2))
                        pygame.display.update()
                        pygame.time.delay(1000)
                    else:
                        WINDOW.blit(background, (0, 0))
                        pygame.display.update()
                        if highscore >= score:
                            save_object(highscore)
                        pygame.mixer.music.fadeout(1000)
                        WINDOW.blit(background, (0, 0))
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
                        main()
                        break

            pygame.mixer.music.pause() if mute else pygame.mixer.music.unpause()  # Pause or unpause the music

        if not running:
            save_object(highscore) if score >= highscore else None
            continue

        draw(playerX, bullets, direction, highscore, highscoreBreak, mute, lives, timeText, scoreText, explosions, dt)

    pygame.quit()


if __name__ == "__main__":
    main()
