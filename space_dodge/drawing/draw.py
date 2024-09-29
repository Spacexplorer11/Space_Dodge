import pygame

# Importing the crucial variables from the constants file
from space_dodge.file_handling.constants_and_file_loading import (WINDOW, WIDTH, HEIGHT, FONT, PLAYER_HEIGHT, BULLET_HEIGHT, playerL, playerR,
                                                                  threeLives, twoLives, oneLife,
                                                                  background, bullet_texture, bullet_explosion_frames,
                                                                  pauseSymbol, muteSymbol, unmuteSymbol)

# Create a mask for the bullet
bullet_mask = pygame.mask.from_surface(bullet_texture)


def draw(playerX, bullets, direction, highscore, highscoreBreak, mute, lives, timeText, scoreText, explosions, dt):
    WINDOW.blit(background, (0, 0))

    # Draw the bullets using the bullet surface
    for bullet in bullets:
        WINDOW.blit(bullet_texture, (bullet.x, bullet.y))
        if bullet.y > HEIGHT - BULLET_HEIGHT - 10:
            explosions.append(Explosion(bullet.x, HEIGHT - BULLET_HEIGHT - 10, list(bullet_explosion_frames.values()), 0.6))

    # Update and draw explosions
    for explosion in explosions:
        explosion.update(dt)
        explosion.draw(WINDOW)
    explosions = [explosion for explosion in explosions if not explosion.is_finished()]

    highScoreTextPt1 = FONT.render(f"Your high score", 1, "white")
    highScoreText_was = FONT.render(f" was {highscore}", 1, "white")
    highScoreText_is = FONT.render(f" is {highscore}", 1, "white")

    WINDOW.blit(timeText, (10, 10))
    WINDOW.blit(scoreText, (WIDTH - 270, 10))
    WINDOW.blit(highScoreTextPt1, (250, 10))
    WINDOW.blit(pauseSymbol, (scoreText.get_width() + 745, 19))

    # Show the mute/unmute symbol
    if mute:
        WINDOW.blit(muteSymbol, (timeText.get_width() + 10, 10))
    else:
        WINDOW.blit(unmuteSymbol, (timeText.get_width() + 10, 10))

    # Check if the highscore is higher than the current score and if it is then say highscore "is" not "was"
    if highscoreBreak:
        WINDOW.blit(highScoreText_is, (500, 10))
    else:
        WINDOW.blit(highScoreText_was, (500, 10))

    # Changing where the player faces
    # 1 = right vs 0 = left
    WINDOW.blit(playerL if direction == 0 else playerR, (playerX, HEIGHT - PLAYER_HEIGHT))

    # Draw the lives
    if lives == 3:
        WINDOW.blit(threeLives, (780, 50))
    elif lives == 2:
        WINDOW.blit(twoLives, (780, 50))
    elif lives == 1:
        WINDOW.blit(oneLife, (780, 50))
    else:
        WINDOW.blit(background, (0, 0))

    pygame.display.update()


class Explosion:
    def __init__(self, x, y, frames, duration):
        self.x = x
        self.y = y
        self.frames = frames
        self.duration = duration
        self.current_frame = 0
        self.time_per_frame = duration / len(frames)
        self.time_accumulator = 0

    def update(self, dt):
        self.time_accumulator += dt
        if self.time_accumulator >= self.time_per_frame:
            self.time_accumulator -= self.time_per_frame
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = len(self.frames)  # Mark as finished

    def draw(self, surface):
        if self.current_frame < len(self.frames):
            surface.blit(self.frames[self.current_frame], (self.x, self.y))

    def is_finished(self):
        return self.current_frame >= len(self.frames) - 1
