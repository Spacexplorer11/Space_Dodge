import pygame

from space_dodge.file_handling.constants_and_file_loading import (
    WINDOW, WIDTH, HEIGHT, FONT, BULLET_HEIGHT,
    threeLives, twoLives, oneLife, background, bullet_texture, bullet_explosion_frames,
    pauseButtonImage, muteImage, unmuteImage
)
from space_dodge.classes.animation import Animation

# Create a mask for the bullet
bullet_mask = pygame.mask.from_surface(bullet_texture)


def draw(player, bullets, direction, highscore, highscoreBreak, mute, lives, timeText, scoreText, explosions, dt):
    WINDOW.blit(background, (0, 0))

    # Draw bullets and add explosions
    for bullet in bullets:
        WINDOW.blit(bullet_texture, (bullet.x, bullet.y))
        if bullet.y > HEIGHT - BULLET_HEIGHT - 10:
            explosions.append(
                Animation(x=bullet.x, y=(HEIGHT - BULLET_HEIGHT - 10), frames=list(bullet_explosion_frames.values()), duration=0.7))

    # Update and draw explosions
    for explosion in explosions:
        explosion.update(dt)
        explosion.draw(WINDOW)
        explosions = [explosion for explosion in explosions if not explosion.is_finished()]

    # Draw texts and symbols
    WINDOW.blit(timeText, (10, 10))
    WINDOW.blit(scoreText, (WIDTH - 270, 10))
    WINDOW.blit(FONT.render("Your high score", 1, "white"), (250, 10))
    WINDOW.blit(pauseButtonImage, (scoreText.get_width() + 745, 19))
    WINDOW.blit(muteImage if mute else unmuteImage, (timeText.get_width() + 10, 10))
    highScoreText = FONT.render(f" is {highscore}" if highscoreBreak else f" was {highscore}", 1, "white")
    WINDOW.blit(highScoreText, (500, 10))

    # Draw player
    WINDOW.blit(player.direction(direction), (player.x, player.y))

    # Draw lives
    lives_images = {3: threeLives, 2: twoLives, 1: oneLife}
    if lives in lives_images:
        WINDOW.blit(lives_images[lives], (780, 50))
    else:
        WINDOW.blit(background, (0, 0))

    pygame.display.update()
