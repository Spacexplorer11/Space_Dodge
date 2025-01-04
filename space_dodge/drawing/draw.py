import pygame

from space_dodge.classes.animation import Animation
from space_dodge.file_handling.constants_and_file_loading import (
    WINDOW, WIDTH, HEIGHT, FONT, BULLET_HEIGHT,
    threeLives, twoLives, oneLife, game_background, bullet_texture, bullet_explosion_frames)

# Create a mask for the bullet
bullet_mask = pygame.mask.from_surface(bullet_texture)


def draw(player, bullets, highscore, highscoreBreak, mute, lives, timeText, scoreText, explosions, dt,
         muteSymbol, unmuteSymbol, pauseButton):
    WINDOW.blit(game_background, (0, 0))

    # Draw bullets and add explosions
    for bullet in bullets:
        WINDOW.blit(bullet_texture, (bullet.x, bullet.y))
        if bullet.y > HEIGHT - BULLET_HEIGHT - 10:
            explosions.append(
                Animation(x=bullet.x, y=(HEIGHT - BULLET_HEIGHT - 10), frames=list(bullet_explosion_frames.values()),
                          duration=0.7))

    # Update and draw explosions
    for explosion in explosions:
        explosion.update(dt)
        explosion.draw(WINDOW)
        explosions = [explosion for explosion in explosions if not explosion.is_finished()]

    # Draw texts and symbols
    WINDOW.blit(timeText, (10, 10))
    WINDOW.blit(scoreText, (WIDTH - 270, 10))
    WINDOW.blit(FONT.render("Your high score", 1, "white"), (250, 10))
    WINDOW.blit(pauseButton.image, (scoreText.get_width() + 745, 19))
    WINDOW.blit(muteSymbol.image if mute else unmuteSymbol.image, (timeText.get_width() + 10, 10))
    highScoreText = FONT.render(f" is {highscore}" if highscoreBreak else f" was {highscore}", 1, "white")
    WINDOW.blit(highScoreText, (500, 10))

    # Draw player
    WINDOW.blit(player.image, player.pos)

    # Draw lives
    lives_images = {3: threeLives,
                    2: twoLives, 1: oneLife}
    if lives in lives_images:
        WINDOW.blit(lives_images[lives], (780, 50))
    else:
        WINDOW.blit(game_background, (0, 0))

    pygame.display.update()
