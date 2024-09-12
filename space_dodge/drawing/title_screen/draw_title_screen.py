import pygame
import os
import logging
from logging import getLogger

from space_dodge.drawing.exception_handling.draw_exception import draw_except
from space_dodge.file_handling.utility import ref

# Window variables
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Button variables
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 200

# Initialise pygame & pygame.mixer
pygame.init()
pygame.mixer.init()

# Declare the logger
logfile = ref('mylog.log')
logging.basicConfig(filename=logfile, level=logging.INFO)
logger = getLogger(__name__)

# Load the title screen image
try:
    title_screen_image = pygame.transform.scale(pygame.image.load(ref("assets/title_screen.jpg")), (WIDTH, HEIGHT))
except FileNotFoundError:
    logger.exception('Title screen image not found')  # log the exception in a file
    error = "Background"
    draw_except(error)

# Load the start button image
try:
    start_button_image = pygame.transform.scale(pygame.image.load(ref("assets/start_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
except FileNotFoundError:
    logger.exception('Start button image not found')  # log the exception in a file
    error = "Button"
    draw_except(error)

# Check if the title screen music file exists
title_screen_music_check = os.path.exists(ref("sounds/background_music/title_screen/title_screen_music.mp3"))
if not title_screen_music_check:
    logger.exception('Title screen music not found')  # log the exception in a file
    error = "Music"
    draw_except(error)

try:
    muteSymbol = pygame.transform.scale(pygame.image.load(ref("assets/mute.png")), (80, 60))
    unmuteSymbol = pygame.transform.scale(pygame.image.load(ref("assets/unmute.png")), (80, 60))
except FileNotFoundError:
    logger.exception('Mute/unmute symbol not found')
    error = "Symbol"
    draw_except(error)

# Define Rect objects
start_button_rect = start_button_image.get_rect(x=WIDTH / 2 - BUTTON_WIDTH / 2, y=HEIGHT / 2 - BUTTON_HEIGHT / 2)
muteSymbol_rect = muteSymbol.get_rect(x=50, y=200, width=80, height=60)
unmuteSymbol_rect = unmuteSymbol.get_rect(x=50, y=200, width=80, height=60)


# Draw the title screen
def draw_title(start):
    # Load the title screen music
    pygame.mixer.music.load(ref("sounds/background_music/title_screen/title_screen_music.mp3"))
    pygame.mixer.music.set_volume(0.5)
    WINDOW.blit(unmuteSymbol, (50, 200))
    pygame.mixer.music.play(loops=-1)
    mute = False
    while not start:
        WINDOW.blit(title_screen_image, (0, 0))
        WINDOW.blit(start_button_image, (WIDTH / 2 - BUTTON_WIDTH / 2, HEIGHT / 2 - BUTTON_HEIGHT / 2))
        WINDOW.blit(muteSymbol if mute else unmuteSymbol, (50, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    start = True
                    welcome = True
                    pygame.mixer.music.stop()
                    return start, welcome
                if muteSymbol_rect.collidepoint(mouse_x, mouse_y) or unmuteSymbol_rect.collidepoint(mouse_x, mouse_y):
                    if mute:
                        mute = False
                        pygame.mixer.music.unpause()
                    else:
                        mute = True
                        pygame.mixer.music.pause()
        pygame.display.update()
